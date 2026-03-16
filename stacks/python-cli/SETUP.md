# Setup

## Prerequisites

- [ ] Python 3.13+ installed
- [ ] [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- [ ] [just](https://github.com/casey/just#installation) installed
- [ ] [pre-commit](https://pre-commit.com/#install) installed
- [ ] [Docker](https://docs.docker.com/get-docker/) installed (for container builds)
- [ ] Git configured with signing (for commitizen / sign-off)

## Scaffold

- [ ] Copy `template/` contents into a new repo root
- [ ] Rename `src/myapp/` directory > `src/<yourapp>/`

## Replace `myapp` > `<yourapp>`

**pyproject.toml:**

- [ ] `project.name`
- [ ] `project.scripts` — key and module path (`<yourapp> = "<yourapp>.cli:entrypoint"`)
- [ ] `tool.hatch.build.targets.wheel.packages` > `["src/<yourapp>"]`
- [ ] `tool.ruff.lint.isort.known-first-party` > `["<yourapp>"]`
- [ ] `tool.coverage.run.source` > `["<yourapp>"]`
- [ ] `tool.commitizen.version_files` > `"src/<yourapp>/__init__.py:__version__"`

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
- [ ] `codecov.yml` — all `paths` entries under flags > `src/<yourapp>/`
- [ ] `Dockerfile` — `ENTRYPOINT ["<yourapp>"]`
- [ ] `.github/workflows/ci.yml` — `docker build -t` and `docker run --rm` image name, `package` job entry-point verification
- [ ] `.github/workflows/release.yml` — `pypi.org/p/<yourapp>` environment URL, `check` job PyPI URL
- [ ] `.github/ISSUE_TEMPLATE/bug_report.yml` — version command, reproduction steps
- [ ] `.github/settings.yml` — `repository.name`
- [ ] `CONTRIBUTING.md` — clone URL repo name, `cd` directory name
- [ ] `docs/index.md` — heading, description, install/usage commands
- [ ] `README.md` (template) — heading, all badge URLs, install commands (`uv`, `pip`, `docker`), usage examples, clone URL, `cd` dir, env var prefix table (`<YOURAPP>_` entries), docs link, star history chart

## Replace `avishj` > `<owner>`

- [ ] `pyproject.toml` — all `project.urls` (Homepage, Documentation, Repository, Changelog, Issues)
- [ ] `mkdocs.yml` — `site_url`, `repo_url`, `repo_name`
- [ ] `README.md` (template) — all badge URLs, clone URL, docs link, star history chart
- [ ] `SECURITY.md` — advisory link
- [ ] `CONTRIBUTING.md` — clone URL, issues link
- [ ] `.github/FUNDING.yml` — `github: [<owner>]`
- [ ] `CODEOWNERS` — `* @<owner>`
- [ ] `.github/settings.yml` — `repository.homepage`

## Replace `${...}` placeholders

- [ ] `sonar-project.properties` — `${SONAR_PROJECT_KEY}`, `${SONAR_ORG}`, `${PROJECT_NAME}`
- [ ] `README.md` (template) — `${SONAR_PROJECT_KEY}` in SonarCloud badge

## Replace other placeholders

- [ ] `pyproject.toml` — `project.description` ("A CLI application.")
- [ ] `pyproject.toml` — `project.authors` (`Your Name`, `you@example.com`)
- [ ] `pyproject.toml` — `project.keywords` (empty list)
- [ ] `pyproject.toml` — `project.license` (if not AGPL-3.0)
- [ ] `pyproject.toml` — `project.classifiers` license classifier (if license changed)
- [ ] `.github/settings.yml` — `repository.description` ("Change This"), `repository.topics` ("change-this")
- [ ] `LICENSE` — replace file if license changed, update copyright holder
- [ ] `README.md` (template) — license badge and footer link (if license changed)
- [ ] `mkdocs.yml` — `copyright` year

## Install & initialize

- [ ] Run `uv sync` — creates venv and installs all deps
- [ ] Run `uv lock` — generates `uv.lock`
- [ ] Run `pre-commit install` — installs git hooks (pre-commit + commit-msg)

## Validate locally

- [ ] `just lint` — ruff check + format passes
- [ ] `just typecheck` — ty check passes
- [ ] `just test` — all tests pass
- [ ] `just cov` — coverage ≥ 70%
- [ ] `just complexity` — no function exceeds max complexity (15)
- [ ] `just build` — sdist + wheel built successfully
- [ ] `just docs` — mkdocs serves without errors

## GitHub repo settings

- [ ] Create GitHub repo (public, default branch `main`)
- [ ] Enable GitHub Pages (source: GitHub Actions) for docs
- [ ] Add repo secret: `CODECOV_TOKEN`
- [ ] Add repo secret: `SONAR_TOKEN`
- [ ] Add repo secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN` (if publishing to Docker Hub)
- [ ] Create GitHub environment: `pypi` (with trusted publisher configured)
- [ ] Enable secret scanning with push protection
- [ ] Enable Dependabot security updates
- [ ] Enable release immutability: Settings > scroll to "Releases" section > select "Enable release immutability" (only applies to future releases)
- [ ] Enable Docker Hub immutable tags: Docker Hub > Repositories > select repo > Settings > General > Tag Mutability > select "Specific tags are immutable" > set regex to `^\d+\.\d+\.\d+$` > save (protects exact semver; keeps `latest`/major/minor mutable)
- [ ] GHCR immutable tags: GHCR does not support immutable tags; Cosign signatures and attestations verify provenance by digest but do not prevent tag repointing; consumers must point to digests where possible
- [ ] Push and verify CI workflow passes
