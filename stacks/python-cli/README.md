# Python CLI

## What this stack is for?

This stack is for building command line tools, scripts and automation utilities in Python. The deliverable is a CLI application that users install and invoke from a terminal, not a web service or library. It covers single command tools as well as multi command CLIs with subcommands, flags and configuration.

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
10. Semgrep - Static analysis (SAST).
11. commitizen - Conventional commits and versioning.
12. Gitleaks - Secret scanner.
13. mkdocs-material - Documentation site generator.
14. editorconfig - Editor consistency config.

## Libraries

1. Typer - CLI framework.
2. rich - Terminal output formatting.
3. pydantic-settings - Typed configuration.

## CI

1. step-security/harden-runner@a90bcbc6539c36a85cdfeb73f7e2f433735f215b # v2.15.0 - Runner hardening.
2. actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2 - Repo checkout.
3. actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0 - Artifact upload.
4. actions/download-artifact@70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3 # v8.0.0 - Artifact download.
5. astral-sh/setup-uv@5a095e7a2014a4212f075830d4f7277575a9d098 # v7.3.1 - Install uv.
6. codecov/codecov-action@671740ac38dd9b0130fbe1cec585b89eea48d3de # v5.5.2 - Coverage upload.
7. github/codeql-action@45580472a5bb82c4681c4ac726cfdb60060c2ee1 # v3.32.4 - Semantic SAST.
8. actions/dependency-review-action@05fe4576374b728f0c523d6a13d64c25081e0803 # v4.8.3 - PR dependency gate.
9. gitleaks/gitleaks-action@ff98106e4c7b2bc287b24eaf42907196329070c7 # v2.3.9 - Secret scanner.
10. ossf/scorecard-action@4eaacf0543bb3f2c246792bd56e8cdeffafb205a # v2.4.3 - Supply chain scoring.
11. anchore/sbom-action@17ae1740179002c89186b61233e0f892c3118b11 # v0.23.0 - SBOM generation.
12. aquasecurity/trivy-action@e368e328979b113139d6f9068e03accaed98a518 # 0.34.1 - Vulnerability scanner.
13. actions/attest@59d89421af93a897026c735860bf21b6eb4f7b26 # v4.1.0 - Build and SBOM attestation.
14. slsa-framework/slsa-github-generator@f7dd8c54c2067bafc12ca7a55595d5ee9b75204a # v2.1.0 - SLSA build attestation.
15. pypa/gh-action-pypi-publish@ed0c53931b1dc9bd32cbe73a98c7f6766f8a527e # v1.13.0 - PyPI publishing.
16. docker/setup-buildx-action@8d2750c68a42422c14e847fe6c8ac0403b4cbd6f # v3.12.0 - Buildx setup.
17. docker/login-action@c94ce9fb468520275223c153574b00df6fe4bcc9 # v3.7.0 - Registry login.
18. docker/build-push-action@10e90e3645eae34f1e60eeb005ba3a3d33f178e8 # v6.19.2 - Container build and push.
19. docker/metadata-action@c299e40c65443455700f0fdfc63efafe5b349051 # v5.10.0 - Container tags and labels.
20. Dependabot - Automated dependency updates (repo config).
21. GitHub secret scanning - Push protection (repo setting).

## Project structure

```
template/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── codeql.yml
│   │   ├── docs.yml
│   │   ├── release.yml
│   │   └── scorecard.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
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
│   ├── __init__.py
│   ├── conftest.py
│   └── test_cli.py
├── .dockerignore
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── Dockerfile
├── LICENSE
├── README.md
├── justfile
├── mkdocs.yml
└── pyproject.toml
```
