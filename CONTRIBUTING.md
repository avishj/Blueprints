<!--
SPDX-FileCopyrightText: 2026 Avish Jha <avish.j@pm.me>

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# Contributing

Thanks for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork:

   ```bash
   git clone https://github.com/<your_username>/blueprints.git
   cd blueprints
   ```

## Development Workflow

1. Create a feature branch from `main`:

   ```bash
   git checkout -b feat/my-feature
   ```

2. Make your changes and verify everything passes locally.

3. Commit using [conventional commits](https://www.conventionalcommits.org/) with a [sign-off](https://developercertificate.org/):

   ```bash
   git commit -s -m "feat: add cool feature"
   ```

4. Push and open a pull request against `main`.

## Guidelines

- **Open an issue first** for non-trivial changes to discuss the approach.
- **Keep PRs focused** with one logical change per PR.
- **Follow existing code style** enforced by CI.

## Verifying changes

Blueprints uses two verification layers:

- **Meta verification** (`.github/workflows/verify-meta.yml`): repo-level security/lint checks plus stack contract validation.
- **Stack verification** (`.github/workflows/verify-stack.yml`): regenerate changed stacks, run preflight (`just install`, `just lint`, `just build`), then smoke-test via `blueprints-smoke-<stack>` push + PR CI.

Entry workflows:

- `ci.yml`: runs meta checks and dispatches stack verification only for changed stacks.
- `weekly.yml`: runs meta checks and stack verification for all stacks on a schedule.

For stack-specific contract examples and local repro commands, refer to each stack’s `stacks/<name>/verify/README.md`.

## Reporting Bugs

Open a [GitHub issue](https://github.com/avishj/blueprints/issues/new) with steps to reproduce.

## Security

See [SECURITY.md](SECURITY.md) for reporting vulnerabilities.
