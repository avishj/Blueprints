<!--
SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# Verify python-cli

These files let CI regenerate the template and prove the result still works.

## Files

- `answers.yml` — Copier inputs. Values match the smoke repo so generated
  names (PyPI, Sonar, Docker) line up.
- `preflight.py` — Runs `uv sync`, ruff, ty, pytest, `uv build`, twine in the
  regenerated project.
- `trigger.py` — Edits a smoke-repo PR branch to fire every path-filtered job
  in the generated `ci.yml`.

## Run locally

```bash
uv tool install copier
copier copy --defaults --vcs-ref=HEAD \
  --data-file stacks/python-cli/verify/answers.yml \
  stacks/python-cli /tmp/python-cli-out
./stacks/python-cli/verify/preflight.py /tmp/python-cli-out
```

## How it runs in CI

On every Blueprints PR, `verify-stack.yml`:

1. Regenerates the template and runs `preflight.py`.
2. Force-pushes the regenerated project to `main` of
   `blueprints-smoke-python-cli` and waits for that repo's CI.
3. Opens a trivial PR there using `trigger.py` and waits for PR CI.
4. Posts a summary back to the Blueprints PR.

`weekly.yml` runs the same flow against `main` on a weekly cron to catch
drift from upstream changes.

## Troubleshooting

- **Push CI failed**: open the linked run on
  `avishj/blueprints-smoke-python-cli`. `main` there reflects the last
  verified PR.
- **PR CI failed**: same repo, look for the open `verify/<run-id>` PR
  (closed automatically on success, kept open on failure for triage).
- **Stale verify branches**: cleanup runs `if: always()`, so stale branches
  mean the cleanup step itself failed — check job logs.

## PAT rotation

`SMOKE_TOKEN` is a fine-grained PAT scoped to `blueprints-smoke-*` with
Contents R/W, Pull requests R/W, Actions R, Metadata R. Expires yearly;
rotate via GitHub -> Settings -> Developer settings -> Fine-grained tokens.
