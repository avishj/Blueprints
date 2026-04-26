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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()

    return subprocess.run(["uv", "sync", "--frozen"], cwd=args.project_dir).returncode


if __name__ == "__main__":
    sys.exit(main())
