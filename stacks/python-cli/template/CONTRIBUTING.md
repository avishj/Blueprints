# Contributing

Thanks for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork and set up the dev environment:

   Install [`just`](https://github.com/casey/just) if not already available, then:

   ```bash
   git clone https://github.com/<your-username>/myapp.git
   cd myapp
   uv sync
   pre-commit install
   ```

## Development Workflow

1. Create a feature branch from `main`:

   ```bash
   git checkout -b feat/my-feature
   ```

2. Make your changes and verify everything passes:

   ```bash
   just ci
   ```

3. Commit using [conventional commits](https://www.conventionalcommits.org/) with a [sign-off](https://developercertificate.org/):

   ```bash
   git commit -s -m "feat: add cool feature"
   ```

4. Push and open a pull request against `main`.

## Guidelines

- **Open an issue first** for non-trivial changes to discuss the approach.
- **Keep PRs focused** with one logical change per PR.
- **Add tests** for new functionality.
- **Follow existing code style** enforced by pre-commit hooks and CI.

## Reporting Bugs

Open a [GitHub issue](https://github.com/avishj/myapp/issues/new/choose) using the appropriate template.

## Security

See [SECURITY.md](SECURITY.md) for reporting vulnerabilities.
