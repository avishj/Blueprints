#!/usr/bin/env -S uv run --script
# SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Helper for `verify-stack.yml` smoke job orchestration.

This file is *not* a workflow — `.github/workflows/` only loads `*.yml`/`*.yaml`.
It is invoked from `run:` steps in `verify-stack.yml` via subcommands, and
centralises the gh CLI subprocess wrapper, `$GITHUB_OUTPUT` writes, and
`$GITHUB_STEP_SUMMARY` appends so the workflow YAML stays declarative.

Subcommands:

- ``wait``: poll smoke-repo CI runs for a SHA until all complete; mirror
  outcomes to the job summary; exit non-zero on failure or timeout.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from typing import Any

OK_CONCLUSIONS = frozenset({"success", "skipped", "neutral"})


# --- shared helpers ---


def gh(*args: str, parse_json: bool = False) -> Any:
    """Run ``gh`` with ``args``; return stdout (parsed as JSON when requested)."""
    proc = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return json.loads(proc.stdout) if parse_json else proc.stdout


def step_summary(markdown: str) -> None:
    """Append ``markdown`` to ``$GITHUB_STEP_SUMMARY`` (no-op outside Actions)."""
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(markdown)


def smoke_repo(stack: str) -> str:
    """Smoke repo slug for a given stack."""
    return f"avishj/blueprints-smoke-{stack}"


def kind_label(kind: str) -> str:
    """Human label for the wait kind in messages and summaries."""
    return "PR" if kind == "pr" else "push"


# --- subcommands ---


def cmd_wait(args: argparse.Namespace) -> int:
    """Poll smoke-repo CI for a SHA until all runs complete; mirror to job summary."""
    repo = smoke_repo(args.stack)
    label = kind_label(args.kind)
    deadline = time.time() + args.timeout
    started = time.time()

    runs: list[dict[str, Any]] = []
    while True:
        runs = gh(
            "run", "list", "--repo", repo, "--commit", args.sha,
            "--json", "databaseId,status,conclusion,name,url",
            parse_json=True,
        )
        elapsed = time.time() - started
        all_done = runs and all(r["status"] == "completed" for r in runs)
        if all_done and elapsed >= args.settle_window:
            break
        if not runs and elapsed > args.settle_window * 2:
            print(
                f"::error::no workflow runs registered for {label} {args.sha} on {repo}",
                file=sys.stderr,
            )
            return 1
        if time.time() > deadline:
            print(
                f"::error::timed out waiting for {label} CI on {repo}@{args.sha}",
                file=sys.stderr,
            )
            return 1
        time.sleep(args.poll_interval)

    summary = [f"## Smoke {label} CI ({repo}@{args.sha[:7]})\n\n"]
    for r in runs:
        icon = "✅" if r["conclusion"] in OK_CONCLUSIONS else "❌"
        summary.append(f"- {icon} [{r['name']}]({r['url']}) — {r['conclusion']}\n")
    step_summary("".join(summary))

    failed = [r for r in runs if r["conclusion"] not in OK_CONCLUSIONS]
    if failed:
        names = ", ".join(r["name"] for r in failed)
        print(
            f"::error::{label} CI failures on {repo}@{args.sha}: {names}",
            file=sys.stderr,
        )
        return 1
    return 0


# --- argparse glue ---


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="smoke", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_wait = sub.add_parser("wait", help="Wait for smoke-repo CI runs to complete.")
    p_wait.add_argument("--stack", required=True)
    p_wait.add_argument("--sha", required=True)
    p_wait.add_argument("--kind", choices=("push", "pr"), required=True)
    p_wait.add_argument("--timeout", type=int, default=20 * 60, help="Seconds.")
    p_wait.add_argument("--poll-interval", type=int, default=15, help="Seconds.")
    p_wait.add_argument(
        "--settle-window",
        type=int,
        default=30,
        help="Min seconds before trusting 'all completed' — lets slower runs register.",
    )
    p_wait.set_defaults(func=cmd_wait)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
