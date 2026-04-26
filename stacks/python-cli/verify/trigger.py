#!/usr/bin/env -S uv run --script
# SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""Make a meaningful change in the smoke-repo PR branch.

Run from cwd of smoke-repo PR branch; produces edits that trigger every
path-filtered workflow in the generated ci.yml.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path


def main() -> int:
    readme = Path("README.md")
    stamp = dt.datetime.now(dt.UTC).isoformat()
    with readme.open("a", encoding="utf-8") as f:
        f.write(f"\n<!-- verify: {stamp} -->\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
