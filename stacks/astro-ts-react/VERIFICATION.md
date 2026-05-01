<!--
SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# Verification

This document defines validation criteria for generated Astro + TS + React projects.

## Acceptance criteria

- Template renders successfully via Copier.
- Generated project installs dependencies with Bun.
- Generated project can run baseline local commands without template failures.
- Generated project contains expected scaffold surfaces for runtime, docs, and tests.

## Checklist skeleton

- [ ] Run Copier interactive scaffold once.
- [ ] Run Copier non-interactive scaffold once.
- [ ] Confirm Bun install task runs.
- [ ] Confirm generated files include expected root docs and starter app files.
- [ ] Confirm follow-up branch verification checks are documented and executable.
