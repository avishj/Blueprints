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

## Libraries

1. Cyclopts - CLI framework.
2. rich - Terminal output formatting.
3. pydantic-settings - Typed configuration.

## CI

1. step-security/harden-runner@58077d3c7e43986b6b15fba718e8ea69e387dfcc # v2.15.1 - Runner hardening.
2. actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2 - Repo checkout.
3. actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0 - Artifact upload.
4. actions/download-artifact@70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3 # v8.0.0 - Artifact download.
5. astral-sh/setup-uv@5a095e7a2014a4212f075830d4f7277575a9d098 # v7.3.1 - Install uv.
6. raven-actions/actionlint@205b530c5d9fa8f44ae9ed59f341a0db994aa6f8 # v2.1.2 - Workflow file linter.
7. codecov/codecov-action@671740ac38dd9b0130fbe1cec585b89eea48d3de # v5.5.2 - Coverage upload.
8. github/codeql-action@0d579ffd059c29b07949a3cce3983f0780820c98 # v4.32.6 - Semantic SAST.
9. actions/dependency-review-action@2031cfc080254a8a887f58cffee85186f0e49e48 # v4.9.0 - PR dependency gate.
10. gitleaks/gitleaks-action@ff98106e4c7b2bc287b24eaf42907196329070c7 # v2.3.9 - Secret scanner.
11. ossf/scorecard-action@4eaacf0543bb3f2c246792bd56e8cdeffafb205a # v2.4.3 - Supply chain scoring.
12. anchore/sbom-action@17ae1740179002c89186b61233e0f892c3118b11 # v0.23.0 - SBOM generation.
13. aquasecurity/trivy-action@57a97c7e7821a5776cebc9bb87c984fa69cba8f1 # v0.35.0 - Vulnerability scanner.
14. actions/attest@59d89421af93a897026c735860bf21b6eb4f7b26 # v4.1.0 - Build and SBOM attestation.
15. slsa-framework/slsa-github-generator@f7dd8c54c2067bafc12ca7a55595d5ee9b75204a # v2.1.0 - SLSA build attestation.
16. pypa/gh-action-pypi-publish@106e0b0b7c337fa67ed433972f777c6357f78598 # v1.13.0 - PyPI publishing.
17. docker/setup-buildx-action@4d04d5d9486b7bd6fa91e7baf45bbb4f8b9deedd # v4.0.0 - Buildx setup.
18. docker/login-action@b45d80f862d83dbcd57f89517bcf500b2ab88fb2 # v4.0.0 - Registry login.
19. docker/build-push-action@d08e5c354a6adb9ed34480a06d141179aa583294 # v7.0.0 - Container build and push.
20. docker/metadata-action@030e881283bb7a6894de51c315a6bfe6a94e05cf # v6.0.0 - Container tags and labels.
21. zizmorcore/zizmor-action@71321a20a9ded102f6e9ce5718a2fcec2c4f70d8 # v0.5.2 - Workflow security scanner.
22. Dependabot - Automated dependency updates (repo config).
23. GitHub secret scanning - Push protection (repo setting).

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
├── README.md
├── SECURITY.md
├── codecov.yml
├── justfile
├── mkdocs.yml
├── pyproject.toml
├── renovate.json
└── sonar-project.properties
```

## Setup

### Prerequisites

- [ ] Python 3.13+ installed
- [ ] [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- [ ] [just](https://github.com/casey/just#installation) installed
- [ ] [pre-commit](https://pre-commit.com/#install) installed
- [ ] [Docker](https://docs.docker.com/get-docker/) installed (for container builds)
- [ ] Git configured with signing (for commitizen / sign-off)

### Scaffold

- [ ] Copy `template/` contents into a new repo root
- [ ] Rename `src/myapp/` directory → `src/<yourapp>/`

### Replace `myapp` → `<yourapp>`

**pyproject.toml:**

- [ ] `project.name`
- [ ] `project.scripts` — key and module path (`<yourapp> = "<yourapp>.cli:entrypoint"`)
- [ ] `tool.hatch.build.targets.wheel.packages` → `["src/<yourapp>"]`
- [ ] `tool.ruff.lint.isort.known-first-party` → `["<yourapp>"]`
- [ ] `tool.coverage.run.source` → `["<yourapp>"]`
- [ ] `tool.commitizen.version_files` → `"src/<yourapp>/__init__.py:__version__"`

**Source code:**

- [ ] `src/<yourapp>/__init__.py` — module docstring
- [ ] `src/<yourapp>/__main__.py` — docstring, `from <yourapp>.cli import app`
- [ ] `src/<yourapp>/cli.py` — imports (`from <yourapp> import ...`, `from <yourapp>.config import ...`), `App(name=..., help=...)`, `main()` docstring
- [ ] `src/<yourapp>/config.py` — `env_prefix="<YOURAPP>_"`

**Tests:**

- [ ] `tests/conftest.py` — `from <yourapp>.cli import app`
- [ ] `tests/unit/test_version.py` — `from <yourapp> import __version__`
- [ ] `tests/unit/test_config.py` — `from <yourapp>.config import Settings`, env var refs (`<YOURAPP>_VERBOSE`)
- [ ] `tests/integration/test_cli.py` — `from <yourapp> import __version__`
- [ ] `tests/e2e/test_entrypoint.py` — subprocess command name, assertion strings

**Config files:**

- [ ] `mkdocs.yml` — `site_name`, `site_description`, `copyright`, `watch` path (`src/<yourapp>`)
- [ ] `codecov.yml` — all `paths` entries under flags → `src/<yourapp>/`
- [ ] `Dockerfile` — `ENTRYPOINT ["<yourapp>"]`
- [ ] `.github/workflows/ci.yml` — `docker build -t` and `docker run --rm` image name
- [ ] `.github/workflows/release.yml` — `pypi.org/p/<yourapp>` environment URL
- [ ] `.github/ISSUE_TEMPLATE/bug_report.yml` — version command, reproduction steps
- [ ] `.github/settings.yml` — `repository.name`
- [ ] `CONTRIBUTING.md` — clone URL repo name, `cd` directory name
- [ ] `docs/index.md` — heading, description, install/usage commands
- [ ] `README.md` (template) — env var prefix table (`<YOURAPP>_` entries)

### Replace `avishj` → `<owner>`

- [ ] `pyproject.toml` — all `project.urls` (Homepage, Documentation, Repository, Changelog, Issues)
- [ ] `mkdocs.yml` — `site_url`, `repo_url`, `repo_name`
- [ ] `README.md` (template) — all badge URLs, clone URL, docs link, star history chart
- [ ] `SECURITY.md` — advisory link
- [ ] `CONTRIBUTING.md` — clone URL, issues link
- [ ] `.github/FUNDING.yml` — `github: [<owner>]`
- [ ] `CODEOWNERS` — `* @<owner>`
- [ ] `.github/settings.yml` — `repository.homepage`

### Replace `${...}` placeholders

- [ ] `sonar-project.properties` — `${SONAR_PROJECT_KEY}`, `${SONAR_ORG}`, `${PROJECT_NAME}`
- [ ] `README.md` (template) — `${SONAR_PROJECT_KEY}` in SonarCloud badge

### Replace other placeholders

- [ ] `pyproject.toml` — `project.description` ("A CLI application.")
- [ ] `pyproject.toml` — `project.authors` (`Your Name`, `you@example.com`)
- [ ] `pyproject.toml` — `project.keywords` (empty list)
- [ ] `pyproject.toml` — `project.license` (if not AGPL-3.0)
- [ ] `pyproject.toml` — `project.classifiers` license classifier (if license changed)
- [ ] `.github/settings.yml` — `repository.description` ("Change This"), `repository.topics` ("change-this")
- [ ] `LICENSE` — replace file if license changed, update copyright holder
- [ ] `README.md` (template) — license badge and footer link (if license changed)
- [ ] `mkdocs.yml` — `copyright` year

### Install & initialize

- [ ] Run `uv sync` — creates venv and installs all deps
- [ ] Run `uv lock` — generates `uv.lock`
- [ ] Run `pre-commit install` — installs git hooks (pre-commit + commit-msg)

### Validate locally

- [ ] `just lint` — ruff check + format passes
- [ ] `just typecheck` — ty check passes
- [ ] `just test` — all tests pass
- [ ] `just cov` — coverage ≥ 70%
- [ ] `just complexity` — no function exceeds max complexity (15)
- [ ] `just build` — sdist + wheel built successfully
- [ ] `just docs` — mkdocs serves without errors

### GitHub repo settings

- [ ] Create GitHub repo (public, default branch `main`)
- [ ] Enable GitHub Pages (source: GitHub Actions) for docs
- [ ] Add repo secret: `CODECOV_TOKEN`
- [ ] Add repo secret: `SONAR_TOKEN`
- [ ] Add repo secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN` (if publishing to Docker Hub)
- [ ] Create GitHub environment: `pypi` (with trusted publisher configured)
- [ ] Enable secret scanning with push protection
- [ ] Enable Dependabot security updates
- [ ] Push and verify CI workflow passes
