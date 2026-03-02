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

1. actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2 - Repo checkout.
2. astral-sh/setup-uv@5a095e7a2014a4212f075830d4f7277575a9d098 # v7.3.1 - Install uv.
3. github/codeql-action@45580472a5bb82c4681c4ac726cfdb60060c2ee1 # v3.32.4 - Semantic SAST.
4. actions/dependency-review-action@05fe4576374b728f0c523d6a13d64c25081e0803 # v4.8.3 - PR dependency gate.
5. ossf/scorecard-action@4eaacf0543bb3f2c246792bd56e8cdeffafb205a # v2.4.3 - Supply chain scoring.
6. anchore/sbom-action@17ae1740179002c89186b61233e0f892c3118b11 # v0.23.0 - SBOM generation.
7. aquasecurity/trivy-action@e368e328979b113139d6f9068e03accaed98a518 # 0.34.1 - Vulnerability scanner.
8. gitleaks/gitleaks-action@ff98106e4c7b2bc287b24eaf42907196329070c7 # v2.3.9 - Secret scanner.
9. actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0 - Artifact upload.
10. actions/attest-build-provenance@a2bbfa25375fe432b6a289bc6b6cd05ecc0c4c32 # v4.1.0 - SLSA provenance.
11. slsa-framework/slsa-github-generator@f7dd8c54c2067bafc12ca7a55595d5ee9b75204a # v2.1.0 - SLSA build attestation.
12. Dependabot - Automated dependency updates (repo config).
13. GitHub secret scanning - Push protection (repo setting).
