#!/usr/bin/env -S uv run --script
# SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Local sanity in regenerated python-cli project.

Called by verify-stack.yml's preflight job after `copier copy` regenerates
the template into a temp directory.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


CHECKS: list[tuple[str, list[str]]] = [
    ("uv sync", ["uv", "sync", "--frozen"]),
    ("ruff check", ["uv", "run", "ruff", "check", "."]),
    ("ruff format", ["uv", "run", "ruff", "format", "--check", "."]),
    ("ty check", ["uv", "run", "ty", "check", "src/", "tests/"]),
    ("pytest unit", ["uv", "run", "pytest", "-m", "unit"]),
    ("uv build", ["uv", "build"]),
    ("twine check", ["uvx", "twine", "check", "dist/*"]),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()

    failed: list[str] = []
    for name, cmd in CHECKS:
        print(f"::group::{name}", flush=True)
        rc = subprocess.run(cmd, cwd=args.project_dir).returncode
        print("::endgroup::", flush=True)
        if rc != 0:
            failed.append(name)

    if failed:
        print(f"::error::preflight failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
