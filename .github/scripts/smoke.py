#!/usr/bin/env -S uv run --script
# SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Helper for `verify-stack.yml` smoke job orchestration.

It is invoked from `run:` steps in `verify-stack.yml` via subcommands.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

OK_CONCLUSIONS = frozenset({"success", "skipped", "neutral"})

GIT_AUTHOR_NAME = "blueprints-verify[bot]"
GIT_AUTHOR_EMAIL = "blueprints-verify@users.noreply.github.com"

WAIT_TIMEOUT_S = 20 * 60
POLL_INTERVAL_S = 15
SETTLE_WINDOW_S = 60


# --- shared helpers ---


def gh(*args: str) -> Any:
    """Run ``gh`` with ``args``; return stdout."""
    proc = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return proc.stdout


def git(*args: str, cwd: Path | None = None) -> str:
    """Run ``git`` with ``args`` in ``cwd``; return stdout."""
    proc = subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, cwd=cwd,
    )
    return proc.stdout


def set_output(key: str, value: str) -> None:
    """Append ``key=value`` to ``$GITHUB_OUTPUT``."""
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as fh:
        fh.write(f"{key}={value}\n")


def step_summary(markdown: str) -> None:
    """Append ``markdown`` to ``$GITHUB_STEP_SUMMARY``."""
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
        fh.write(markdown)


def smoke_repo(stack: str) -> str:
    """Smoke repo slug for a given stack."""
    return f"avishj/blueprints-smoke-{stack}"


# --- subcommands ---


def cmd_wait(args: argparse.Namespace) -> int:
    """Poll smoke-repo CI for a SHA until all runs complete; mirror to job summary."""
    repo = smoke_repo(args.stack)
    deadline = time.time() + WAIT_TIMEOUT_S
    started = time.time()

    runs: list[dict[str, Any]] = []
    while True:
        runs = json.loads(gh(
            "run", "list", "--repo", repo, "--commit", args.sha,
            "--json", "databaseId,status,conclusion,name,url",
        ))
        elapsed = time.time() - started
        all_done = runs and all(r["status"] == "completed" for r in runs)
        if all_done and elapsed >= SETTLE_WINDOW_S:
            break
        if time.time() > deadline:
            print(
                f"::error::timed out waiting for smoke CI on {repo}@{args.sha}",
                file=sys.stderr,
            )
            return 1
        time.sleep(POLL_INTERVAL_S)

    summary = [f"## Smoke CI ({repo}@{args.sha[:7]})\n\n"]
    for r in runs:
        icon = "✅" if r["conclusion"] in OK_CONCLUSIONS else "❌"
        summary.append(f"- {icon} [{r['name']}]({r['url']}) — {r['conclusion']}\n")
    step_summary("".join(summary))

    failed = [r for r in runs if r["conclusion"] not in OK_CONCLUSIONS]
    if failed:
        names = ", ".join(r["name"] for r in failed)
        print(
            f"::error::smoke CI failures on {repo}@{args.sha}: {names}",
            file=sys.stderr,
        )
        return 1
    return 0


def cmd_open_pr(args: argparse.Namespace) -> int:
    """Clone smoke repo, run the stack trigger, push a verify branch, open the PR."""
    repo = smoke_repo(args.stack)
    run_id = os.environ["GITHUB_RUN_ID"]
    branch = f"verify/{run_id}"
    workspace = Path(os.environ["GITHUB_WORKSPACE"])
    trigger = workspace / "stacks" / args.stack / "verify" / "trigger.py"
    clone_dir = Path("/tmp/smoke-clone")

    gh("repo", "clone", repo, str(clone_dir), "--", "--depth", "1")

    git("config", "user.name", GIT_AUTHOR_NAME, cwd=clone_dir)
    git("config", "user.email", GIT_AUTHOR_EMAIL, cwd=clone_dir)
    git("switch", "-c", branch, cwd=clone_dir)
    trigger_env = {k: v for k, v in os.environ.items() if k not in {"GH_TOKEN", "GITHUB_TOKEN"}}
    subprocess.run([str(trigger)], cwd=clone_dir, check=True, env=trigger_env)
    git("add", "-A", cwd=clone_dir)
    git("commit", "--quiet", "-m", f"verify: trigger run {run_id}", cwd=clone_dir)
    git("push", "--quiet", "--set-upstream", "origin", branch, cwd=clone_dir)

    pr_url = gh(
        "pr", "create",
        "--repo", repo,
        "--base", "main",
        "--head", branch,
        "--title", f"verify: {run_id}",
        "--body", f"Automated verify PR from Blueprints run {run_id}.",
    ).strip()
    sha = git("rev-parse", "HEAD", cwd=clone_dir).strip()

    set_output("url", pr_url)
    set_output("sha", sha)
    return 0


def cmd_cleanup(args: argparse.Namespace) -> int:
    """Delete the verify branch (auto-closes its PR). Never fails."""
    repo = smoke_repo(args.stack)
    branch = f"verify/{os.environ['GITHUB_RUN_ID']}"
    try:
        gh("api", "-X", "DELETE", f"repos/{repo}/git/refs/heads/{branch}")
    except subprocess.CalledProcessError:
        # Idempotent: branch already deleted is fine.
        pass
    return 0


def _outcome_icon(outcome: str) -> str:
    return "✅" if outcome == "success" else "❌"


def cmd_comment(args: argparse.Namespace) -> int:
    """Render and idempotently upsert the rolling smoke comment on the Blueprints PR."""
    repo = os.environ["GITHUB_REPOSITORY"]
    marker = f"<!-- blueprints-smoke-{args.stack} -->"
    body = "\n".join([
        marker,
        f"### Smoke: `{args.stack}`",
        "",
        f"- {_outcome_icon(args.push_outcome)} push CI",
        f"- {_outcome_icon(args.pr_outcome)} PR CI",
        "",
        f"Verify run: {args.run_url}",
        f"Smoke PR: {args.smoke_pr_url or '_not opened_'}",
        f"Ref: `{args.ref}`",
        "",
    ])

    jq_filter = (
        '.[] | select(.user.login=="github-actions[bot]" '
        f'and (.body | contains("{marker}"))) | .id'
    )
    existing_ids = gh(
        "api", "--paginate", f"repos/{repo}/issues/{args.blueprints_pr}/comments",
        "--jq", jq_filter,
    ).split()

    if existing_ids:
        endpoint = ["api", "-X", "PATCH", f"repos/{repo}/issues/comments/{existing_ids[0]}"]
    else:
        endpoint = ["api", "-X", "POST", f"repos/{repo}/issues/{args.blueprints_pr}/comments"]

    # Stream body via stdin so we don't have to manage a tempfile.
    subprocess.run(
        ["gh", *endpoint, "-F", "body=@-"],
        input=body, text=True, check=True,
    )
    return 0


# --- argparse glue ---


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stack", required=True)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_wait = sub.add_parser("wait", help="Wait for smoke-repo CI runs to complete.")
    p_wait.add_argument("--sha", required=True)
    p_wait.set_defaults(func=cmd_wait)

    p_pr = sub.add_parser("open-pr", help="Open the verify PR on the smoke repo.")
    p_pr.set_defaults(func=cmd_open_pr)

    p_cleanup = sub.add_parser("cleanup", help="Delete the verify branch on the smoke repo.")
    p_cleanup.set_defaults(func=cmd_cleanup)

    p_comment = sub.add_parser("comment", help="Upsert the smoke summary comment on the Blueprints PR.")
    p_comment.add_argument("--ref", required=True)
    p_comment.add_argument("--push-outcome", required=True, help="steps.push-ci.outcome")
    p_comment.add_argument("--pr-outcome", required=True, help="steps.pr-ci.outcome")
    p_comment.add_argument("--smoke-pr-url", default="", help="Empty when no PR was opened.")
    p_comment.add_argument("--run-url", required=True, help="URL of this verify run.")
    p_comment.add_argument("--blueprints-pr", required=True, help="Blueprints PR number to comment on.")
    p_comment.set_defaults(func=cmd_comment)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
