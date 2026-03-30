# Python CLI

## What is this stack for?

This stack is for building command-line tools, scripts, and automation utilities in Python. The deliverable is a CLI application that users install and invoke from a terminal, not a web service or library. It covers single-command tools as well as multi-command CLIs with subcommands, flags, and configuration.

## Usage

This stack is a [Copier](https://copier.readthedocs.io/) template. Scaffold a new project:

```bash
git clone https://github.com/avishj/blueprints /tmp/blueprints
uvx copier copy /tmp/blueprints/stacks/python-cli my-project --trust
rm -rf /tmp/blueprints
```

See [SETUP.md](SETUP.md) for prerequisites, variable reference, non-interactive usage, and GitHub repo configuration.

## Tooling

1. uv - Package manager.
2. Ruff - Linter and formatter.
3. ty - Type checker.
4. pytest - Test framework.
5. pytest-cov - Coverage reporting.
6. pytest-xdist - Parallel test execution.
7. just - Task runner.
8. pre-commit - Git hook framework.
9. complexipy - Cognitive complexity checker.
10. commitizen - Conventional commits and versioning.
11. Gitleaks - Secret scanner.
12. OSV-Scanner - Dependency vulnerability scanner.
13. mkdocs-material - Documentation site generator.
14. editorconfig - Editor consistency config.
15. REUSE - SPDX license/copyright compliance checker.
16. semgrep - Static application security testing.
17. validate-pyproject - pyproject.toml validation.
18. twine - Package validation.

## Libraries

1. Cyclopts - CLI framework.
2. rich - Terminal output formatting.
3. pydantic-settings - Typed configuration.

## Development Environment

**VS Code** — Preconfigured workspace settings, recommended extensions, and a debug launch configuration. Open the project and everything just works.

**Dev Container** — One-click setup for GitHub Codespaces or VS Code Dev Containers. Opens a ready-to-code environment with all tools and dependencies pre-installed.

## CI

1. step-security/harden-runner - Runner hardening.
2. actions/checkout - Repo checkout.
3. dorny/paths-filter - Job gating by changed paths.
4. avishj/blueprints/stacks/python-cli/actions/setup - Shared setup (harden runner + checkout + `setup-uv` + `uv sync --frozen`).
5. actions/upload-artifact - Artifact upload.
6. actions/download-artifact - Artifact download.
7. actions/deploy-pages - GitHub Pages deployment.
8. actions/upload-pages-artifact - Pages artifact upload.
9. actions/labeler - PR auto-labeler.
10. astral-sh/setup-uv - Install uv.
11. raven-actions/actionlint - Workflow file linter.
12. codecov/codecov-action - Coverage upload.
13. github/codeql-action - Semantic SAST.
14. semgrep - Static application security testing (via container).
15. actions/dependency-review-action - PR dependency gate.
16. gitleaks/gitleaks-action - Secret scanner.
17. ossf/scorecard-action - Supply chain scoring.
18. anchore/sbom-action - SBOM generation.
19. aquasecurity/trivy-action - Vulnerability scanner.
20. actions/attest - Build and SBOM attestation.
21. pypa/gh-action-pypi-publish - PyPI publishing.
22. docker/setup-buildx-action - Buildx setup.
23. docker/login-action - Registry login.
24. docker/build-push-action - Container build and push.
25. docker/metadata-action - Container tags and labels.
26. zizmorcore/zizmor-action - Workflow security scanner.
27. sigstore/cosign-installer - Container image signing.
28. google/osv-scanner-action/osv-scanner-action - Dependency vulnerability scanner.
29. google/osv-scanner-action/osv-reporter-action - Vulnerability scan reporter.
30. SonarSource/sonarqube-scan-action - SonarCloud analysis.
31. hadolint/hadolint-action - Dockerfile linter.
32. lycheeverse/lychee-action - Link checker.
33. DavidAnson/markdownlint-cli2-action - Markdown linter.
34. crate-ci/typos - Spell checker.
35. fsfe/reuse-action - REUSE/SPDX compliance check.
36. Renovate - Automated dependency updates (primary, via `renovate.json`).
37. Dependabot - Urgent security advisories only (GitHub-native repo setting).
38. GitHub secret scanning - Push protection (repo setting).

## Project structure

Files with `.jinja` suffix are Copier templates — the suffix is stripped during scaffolding. `{{ module_name }}` and other `{{ }}` directory/file names are rendered from user answers.

```text
stacks/python-cli/
├── copier.yml                         # Copier config (questions, derived vars, tasks)
├── template/
│   ├── {{ _copier_conf.answers_file }}.jinja  # Copier answers (auto-generated)
│   ├── .github/
│   │   ├── ISSUE_TEMPLATE/
│   │   │   ├── bug_report.yml.jinja
│   │   │   └── feature_request.yml.jinja
│   │   ├── workflows/
│   │   │   ├── _codeql.yml.jinja
│   │   │   ├── _osv-scanner.yml.jinja
│   │   │   ├── _security.yml.jinja
│   │   │   ├── _trivy-image.yml.jinja
│   │   │   ├── ci.yml.jinja
│   │   │   ├── docs.yml.jinja
│   │   │   ├── labeler.yml.jinja
│   │   │   ├── release.yml.jinja
│   │   │   └── weekly.yml.jinja
│   │   ├── FUNDING.yml.jinja
│   │   ├── labeler.yml.jinja
│   │   ├── PULL_REQUEST_TEMPLATE.md.jinja
│   │   └── settings.yml.jinja
│   ├── docs/
│   │   └── index.md.jinja
│   ├── src/
│   │   └── {{ module_name }}/
│   │       ├── __init__.py.jinja
│   │       ├── __main__.py.jinja
│   │       ├── cli.py.jinja
│   │       ├── config.py.jinja
│   │       ├── exit_codes.py.jinja
│   │       ├── logging.py.jinja
│   │       └── py.typed
│   ├── tests/
│   │   ├── e2e/
│   │   │   ├── __init__.py.jinja
│   │   │   └── test_entrypoint.py.jinja
│   │   ├── integration/
│   │   │   ├── __init__.py.jinja
│   │   │   └── test_cli.py.jinja
│   │   ├── unit/
│   │   │   ├── __init__.py.jinja
│   │   │   ├── test_config.py.jinja
│   │   │   ├── test_exit_codes.py.jinja
│   │   │   ├── test_logging.py.jinja
│   │   │   └── test_version.py.jinja
│   │   ├── __init__.py.jinja
│   │   └── conftest.py.jinja
│   ├── .devcontainer/
│   │   ├── devcontainer.json.jinja
│   │   └── Dockerfile.jinja
│   ├── .vscode/
│   │   ├── extensions.json
│   │   ├── launch.json.jinja
│   │   └── settings.json
│   ├── .dockerignore.jinja
│   ├── .editorconfig.jinja
│   ├── .gitattributes.jinja
│   ├── .gitignore.jinja
│   ├── .pre-commit-config.yaml.jinja
│   ├── CHANGELOG.md.jinja
│   ├── CODEOWNERS.jinja
│   ├── CONTRIBUTING.md.jinja
│   ├── Dockerfile.jinja
│   ├── LICENSE
│   ├── LICENSES/
│   │   └── AGPL-3.0-or-later.txt
│   ├── README.md.jinja
│   ├── REUSE.toml.jinja
│   ├── SECURITY.md.jinja
│   ├── codecov.yml.jinja
│   ├── justfile.jinja
│   ├── mkdocs.yml.jinja
│   ├── pyproject.toml.jinja
│   ├── renovate.json
│   └── sonar-project.properties.jinja
├── README.md
├── SETUP.md
└── VERIFICATION.md
```
