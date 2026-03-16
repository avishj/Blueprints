# Python CLI

## What is this stack for?

This stack is for building command-line tools, scripts, and automation utilities in Python. The deliverable is a CLI application that users install and invoke from a terminal, not a web service or library. It covers single-command tools as well as multi-command CLIs with subcommands, flags, and configuration.

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
12. mkdocs-material - Documentation site generator.
13. editorconfig - Editor consistency config.
14. REUSE - SPDX license/copyright compliance checker.

## Libraries

1. Cyclopts - CLI framework.
2. rich - Terminal output formatting.
3. pydantic-settings - Typed configuration.

## CI

1. step-security/harden-runner@58077d3c7e43986b6b15fba718e8ea69e387dfcc # v2.15.1 - Runner hardening.
2. actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2 - Repo checkout.
3. actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0 - Artifact upload.
4. actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1 - Artifact download.
5. astral-sh/setup-uv@e06108dd0aef18192324c70427afc47652e63a82 # v7.5.0 - Install uv.
6. raven-actions/actionlint@205b530c5d9fa8f44ae9ed59f341a0db994aa6f8 # v2.1.2 - Workflow file linter.
7. codecov/codecov-action@671740ac38dd9b0130fbe1cec585b89eea48d3de # v5.5.2 - Coverage upload.
8. github/codeql-action@0d579ffd059c29b07949a3cce3983f0780820c98 # v4.32.6 - Semantic SAST.
9. actions/dependency-review-action@2031cfc080254a8a887f58cffee85186f0e49e48 # v4.9.0 - PR dependency gate.
10. gitleaks/gitleaks-action@ff98106e4c7b2bc287b24eaf42907196329070c7 # v2.3.9 - Secret scanner.
11. ossf/scorecard-action@4eaacf0543bb3f2c246792bd56e8cdeffafb205a # v2.4.3 - Supply chain scoring.
12. anchore/sbom-action@57aae528053a48a3f6235f2d9461b05fbcb7366d # v0.23.1 - SBOM generation.
13. aquasecurity/trivy-action@57a97c7e7821a5776cebc9bb87c984fa69cba8f1 # v0.35.0 - Vulnerability scanner.
14. actions/attest@59d89421af93a897026c735860bf21b6eb4f7b26 # v4.1.0 - Build and SBOM attestation.
15. slsa-framework/slsa-github-generator@f7dd8c54c2067bafc12ca7a55595d5ee9b75204a # v2.1.0 - SLSA build attestation.
16. pypa/gh-action-pypi-publish@106e0b0b7c337fa67ed433972f777c6357f78598 # v1.13.0 - PyPI publishing.
17. docker/setup-buildx-action@4d04d5d9486b7bd6fa91e7baf45bbb4f8b9deedd # v4.0.0 - Buildx setup.
18. docker/login-action@b45d80f862d83dbcd57f89517bcf500b2ab88fb2 # v4.0.0 - Registry login.
19. docker/build-push-action@d08e5c354a6adb9ed34480a06d141179aa583294 # v7.0.0 - Container build and push.
20. docker/metadata-action@030e881283bb7a6894de51c315a6bfe6a94e05cf # v6.0.0 - Container tags and labels.
21. zizmorcore/zizmor-action@71321a20a9ded102f6e9ce5718a2fcec2c4f70d8 # v0.5.2 - Workflow security scanner.
22. sigstore/cosign-installer@ba7bc0a3fef59531c69a25acd34668d6d3fe6f22 # v4.1.0 - Container image signing.
23. Renovate - Automated dependency updates (primary, via `renovate.json`).
24. Dependabot - Urgent security advisories only (GitHub-native repo setting).
25. GitHub secret scanning - Push protection (repo setting).
26. fsfe/reuse-action@676e2d560c9a403aa252096d99fcab3e1132b0f5 # v6.0.0 - REUSE/SPDX compliance check.

## Project structure

```text
template/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── workflows/
│   │   ├── _codeql.yml
│   │   ├── _security.yml
│   │   ├── _trivy-image.yml
│   │   ├── ci.yml
│   │   ├── docs.yml
│   │   ├── labeler.yml
│   │   ├── release.yml
│   │   └── weekly.yml
│   ├── FUNDING.yml
│   ├── labeler.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── settings.yml
├── docs/
│   └── index.md
├── src/
│   └── myapp/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       └── py.typed
├── tests/
│   ├── e2e/
│   │   ├── __init__.py
│   │   └── test_entrypoint.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_cli.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_config.py
│   │   └── test_version.py
│   ├── __init__.py
│   └── conftest.py
├── .dockerignore
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CODEOWNERS
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── LICENSES/
│   └── AGPL-3.0-or-later.txt
├── README.md
├── REUSE.toml
├── SECURITY.md
├── codecov.yml
├── justfile
├── mkdocs.yml
├── pyproject.toml
├── renovate.json
└── sonar-project.properties
```