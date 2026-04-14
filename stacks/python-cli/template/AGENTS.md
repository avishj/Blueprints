<!--
SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# MUST FOLLOW RULES

1. MUST ALWAYS use uv for all python related commands.
2. MUST ALWAYS run commands with rtk command, every command is guaranteed to be proxied through it.
3. MUST ALWAYS use skill before git add/commit.
4. MUST ALWAYS add and commit in the same command (both need their own rtk).
5. Pre-commit failure ALWAYS BLOCKS commit. Fix unless autofixed and retry commit.
