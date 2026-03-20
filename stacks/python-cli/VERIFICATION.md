# Verification

## AI Scope

### Section 1 — Project Metadata (`pyproject.toml`)

**Build & packaging:**

- [ ] Build system uses hatchling (`[build-system]` matches template)
- [ ] `project.name` is the actual app name (no `myapp` remnants)
- [ ] `project.description`, `authors`, `keywords` are filled in (not template placeholders)
- [ ] `project.license` and matching `classifiers` entry are consistent
- [ ] All template `classifiers` retained (`Console`, `Typed`, Python versions, etc.)
- [ ] `project.scripts` entry point: key = app name, value = `<app>.cli:entrypoint`
- [ ] All 5 `project.urls` point to the correct repo (no `myapp` remnants)
- [ ] `dependencies` includes `cyclopts`, `rich`, `pydantic-settings` (plus any project additions)
- [ ] `tool.hatch.build.targets.wheel.packages` points to `src/<app>`

**Dev dependencies:**

- [ ] `[dependency-groups]` `dev` contains all 10 template deps (versions may differ, none removed)

**Tooling config — must match template exactly:**

- [ ] `[tool.uv]` section present and unchanged
- [ ] `[tool.ruff]` — `target-version`, `line-length` 88, `src` includes both `src` and `tests`
- [ ] `[tool.ruff.lint]` — all 40+ rule groups in `select`, all 6 in `ignore`
- [ ] `[tool.ruff.lint.per-file-ignores]` — test relaxations (7 rules) present
- [ ] `[tool.ruff.lint.pydocstyle]` — google convention
- [ ] `[tool.ruff.lint.mccabe]` — max-complexity 15
- [ ] `[tool.ty]` — python-version 3.13
- [ ] `[tool.pytest.ini_options]` — `testpaths`, `pythonpath`, `addopts`, all 3 markers, `filterwarnings`, `xfail_strict`
- [ ] `[tool.coverage.run]` — `branch`, `parallel`, `relative_files` all true
- [ ] `[tool.coverage.report]` — `fail_under` 70, all 6 `exclude_lines` patterns

**Tooling config — app-name-dependent (no `myapp` remnants):**

- [ ] `tool.ruff.lint.isort.known-first-party` uses app name
- [ ] `tool.coverage.run.source` uses app name
- [ ] `tool.commitizen.version_files` points to `src/<app>/__init__.py:__version__`

**Commitizen:**

- [ ] `[tool.commitizen]` section present — `tag_format`, `changelog_file`, `update_changelog_on_bump` match template

### Section 2 — Source Code (`src/<yourapp>/`)

- [ ] Directory renamed from `src/myapp/` to `src/<app>/`
- [ ] `py.typed` marker file exists (empty file, copy 1:1)

**`__init__.py`:**

- [ ] Module docstring updated to app name
- [ ] `__version__` variable defined (commitizen manages this)

**`__main__.py`:**

- [ ] Docstring references app name (`Allow running as \`python -m <app>\``)
- [ ] Imports `app` from `<app>.cli` (no `myapp` remnants)
- [ ] Calls `app.meta()`

**`cli.py`:**

- [ ] Imports `__version__` from `<app>` and `settings` from `<app>.config`
- [ ] `App()` created with `name=`, `help=`, `version=__version__`, `version_flags=["--version", "-V"]`
- [ ] `console = Console()` instantiated
- [ ] `@app.meta.default` function exists — wires `--verbose` flag to `settings.verbose` and calls `app(tokens)`
- [ ] `entrypoint()` function exists — calls `app.meta()` (this is the `console_scripts` target)
- [ ] No `myapp` strings remain in `App(name=...)`, `App(help=...)`, or docstrings
- [ ] Demo command (`hello`) may be replaced, but at least one `@app.command` should exist

**`config.py`:**

- [ ] `Settings` class extends `BaseSettings` with `SettingsConfigDict`
- [ ] `env_prefix` set to `<APP>_` (uppercase app name + underscore, not `MYAPP_`)
- [ ] `env_file` and `env_file_encoding` settings present
- [ ] `verbose: bool = False` field exists (used by CLI `--verbose` flag)
- [ ] Module-level `settings = Settings()` instance exported

### Section 3 — Tests

**Directory structure:**

- [ ] `tests/__init__.py` exists (empty)
- [ ] `tests/unit/__init__.py`, `tests/integration/__init__.py`, `tests/e2e/__init__.py` exist (empty)
- [ ] All three test tiers present: `unit/`, `integration/`, `e2e/`

**`conftest.py`:**

- [ ] `CliResult` helper class exists with `exit_code` and `output` attrs
- [ ] `invoke` fixture exists — wraps `app.meta()` calls with capsys capture and SystemExit handling
- [ ] Imports `app` from `<app>.cli` (no `myapp` remnants)

**`unit/test_version.py`:**

- [ ] `pytestmark = pytest.mark.unit` set
- [ ] Imports `__version__` from `<app>` (no `myapp`)
- [ ] Tests that `__version__` is a string and valid semver — these are mandatory, not demo

**`unit/test_config.py`:**

- [ ] `pytestmark = pytest.mark.unit` set
- [ ] Imports `Settings` from `<app>.config` (no `myapp`)
- [ ] Tests default values, env prefix loading, and that unprefixed env vars are ignored
- [ ] All env var references use `<APP>_` prefix (not `MYAPP_`)

**`integration/test_cli.py`:**

- [ ] `pytestmark = pytest.mark.integration` set
- [ ] Imports `__version__` from `<app>` (no `myapp`)
- [ ] Uses `invoke` fixture from conftest
- [ ] `test_version` — mandatory: asserts `--version` exits 0 and output contains `__version__`
- [ ] `test_no_args` — mandatory: asserts bare invocation exits 0 and shows usage
- [ ] `test_hello` — demo (replace with actual command tests)

**`e2e/test_entrypoint.py`:**

- [ ] `pytestmark = pytest.mark.e2e` set
- [ ] `_run()` helper invokes the CLI binary via `subprocess.run` — command name must be app name (not `myapp`)
- [ ] `test_version_flag` — mandatory: subprocess `--version` exits 0
- [ ] `test_no_args_shows_help` — mandatory: bare invocation exits 0 with usage output
- [ ] `test_invalid_command` — mandatory: unknown subcommand exits non-zero
- [ ] `test_hello_command` — demo (replace with actual command tests)
- [ ] No `myapp` string remnants in subprocess calls or assertions

### Section 4 — Docs & Community

**`docs/index.md`:**

- [ ] Heading, description, install command, and quick-start command all use app name (no `myapp`)
- [ ] Structure matches template (Installation + Quick start sections at minimum)

**`mkdocs.yml`:**

- [ ] `site_name`, `site_description` use app name (no `myapp`)
- [ ] `site_url`, `repo_url`, `repo_name` point to correct owner/repo
- [ ] `copyright` has correct year and project name
- [ ] `watch` path points to `src/<app>` (not `src/myapp`)
- [ ] `edit_uri` is `edit/main/docs/`
- [ ] All remaining config (theme, plugins, markdown_extensions, nav) matches template exactly

**`README.md` (template):**

- [ ] All badge URLs use correct owner/repo (no `myapp` remnants in GitHub, PyPI, Docker, Scorecard URLs)
- [ ] `${SONAR_PROJECT_KEY}` in SonarCloud badge replaced with actual key
- [ ] Description updated (not `"A CLI application."`)
- [ ] Features section retained (Cyclopts, Rich, pydantic-settings, py.typed, Python 3.13+)
- [ ] Install commands use app name (uv, pip, docker)
- [ ] Usage examples updated for actual commands (demo `hello` command replaced)
- [ ] Development section: clone URL, `cd` dir use correct repo name
- [ ] Common tasks table matches template (`just lint`, `just typecheck`, `just validate`, `just package-check`, `just reuse-check`, `just pre-commit`, etc.)
- [ ] Configuration section: env var prefix and table use `<APP>_` (not `MYAPP_`), rows updated for actual settings
- [ ] Documentation link points to correct GitHub Pages URL
- [ ] License section matches `pyproject.toml` license choice
- [ ] Star History chart URL uses correct owner/repo

**`CONTRIBUTING.md`:**

- [ ] Clone URL and `cd` dir use correct repo name (no `myapp`)
- [ ] Issues link at bottom uses correct owner/repo
- [ ] All remaining content (workflow steps, guidelines, IDE integration, security ref) matches template

**`SECURITY.md`:**

- [ ] Advisory link uses correct owner/repo (no `myapp`)
- [ ] Rest of file matches template exactly

**`CHANGELOG.md`:**

- [ ] File exists — copy 1:1 from template (commitizen manages content)

**`LICENSE`:**

- [ ] File present — copy 1:1 from template (AGPL-3.0) unless a different license is chosen
- [ ] If license changed: replace file entirely, and update `pyproject.toml` license field, classifiers, README badge, and README footer to match

**Inline SPDX headers (all commentable files):**

- [ ] Every commentable file (`.py`, `.yml`, `.yaml`, `.toml`, `.md`, `.properties`, `Dockerfile`, `justfile`, `CODEOWNERS`, dotfiles) has `SPDX-FileCopyrightText` and `SPDX-License-Identifier` in a comment header
- [ ] Copyright holder and year are updated (not `Avish J <avish.j@pm.me>` unless that is the actual holder)
- [ ] License identifier matches the project license (AGPL-3.0-or-later unless changed)

**`REUSE.toml`:**

- [ ] `version = 1` present
- [ ] Covers only uncommentable files: `*.json`, `*.lock`, `src/myapp/py.typed` (replace `myapp` with your actual package name)
- [ ] `SPDX-FileCopyrightText` entries use actual copyright holder (not `Avish J <avish.j@pm.me>`)
- [ ] `SPDX-License-Identifier` entries match the project license (AGPL-3.0-or-later unless changed)
- [ ] `LICENSES/**` annotation present with FSF copyright

**`LICENSES/` directory:**

- [ ] `LICENSES/AGPL-3.0-or-later.txt` exists with full license text (not a placeholder)
- [ ] If license changed: corresponding `LICENSES/<SPDX-ID>.txt` file exists, old one removed
- [ ] No extra license files for licenses not used by any file

**`CODEOWNERS`:**

- [ ] File exists with `* @<owner>` or another valid ownership entry

### Section 5 — CI/CD Workflows (`.github/workflows/`)

**Reusable workflows (copy 1:1 from template):**

- [ ] `_codeql.yml` — CodeQL analysis with `security-and-quality` queries, paths-ignore for docs/tests, threat models configured, and shared Python setup action usage
- [ ] `_osv-scanner.yml` — OSV dependency vulnerability scanner with CI differential scanning and weekly full-repo scanning modes, SARIF upload
- [ ] `_security.yml` — Semgrep SAST, Trivy filesystem scan, Gitleaks secret scan, zizmor workflow security scan
- [ ] `_trivy-image.yml` — reusable Trivy container image scan with SARIF upload

**Local workflow actions:**

- [ ] `.github/actions/setup-python-env/action.yml` exists — wraps `astral-sh/setup-uv` and `uv sync --frozen`
- [ ] `.github/actions/setup-python-env/action.yml` defaults `python-version` to `3.13` or whatever we use in the `pyproject.toml`

**`ci.yml`:**

- [ ] All 17 jobs present: `changes`, `lint`, `actionlint`, `docker`, `lychee`, `test`, `sonarcloud`, `package`, `complexity`, `security`, `codeql`, `osv-scanner`, `dependency-review`, `reuse`, `config-validation`, `markdownlint`, `ci-passed`
- [ ] `changes` job — uses `dorny/paths-filter` and exposes `python`, `docker`, `docs`, `workflows`, `config`, and `changed_config_files` outputs
- [ ] `lint` job — uses the shared Python setup action, then runs ruff check, ruff format, ty check, validate-pyproject, mkdocs build --strict, and typos spell check
- [ ] `actionlint` job — gated on workflow changes only
- [ ] `docker` job — gated on `docker || workflows`, and `docker build -t` / `docker run --rm` image name uses app name (not `myapp`)
- [ ] `test` job — uses the shared Python setup action, is gated on `python || workflows`, and runs the `3.13` + `3.14` × `ubuntu` + `macos` + `windows` matrix with all 3 test tiers and per-tier Codecov uploads (`unit`, `integration`, `e2e`)
- [ ] `sonarcloud` job — downloads test results and coverage artifacts, then runs SonarCloud scan
- [ ] `package` job — uses the shared Python setup action, is gated on `python || docs || workflows`, and `uv run --with dist/*.whl --no-project --` entry-point verification uses app name (not `myapp`)
- [ ] `complexity` job — uses the shared Python setup action, is gated on `python || workflows`, and runs complexipy with max-complexity 15 plus SARIF upload
- [ ] `config-validation` job — uses the shared Python setup action and is gated on `config`
- [ ] `markdownlint` job — gated on `docs`
- [ ] `ci-passed` gate job — `needs` lists all 16 other jobs and fails only on `failure` or `cancelled` results
- [ ] `osv-scanner` job — calls `_osv-scanner.yml` with `scan-mode: ci`, `security-events: write` permission
- [ ] `dependency-review` job — PR-only, `fail-on-severity: moderate`, license and vuln checks, SSPL/BUSL denied
- [ ] `reuse` job — runs `fsfe/reuse-action` with `--include-submodules lint`, no permissions needed
- [ ] All remaining jobs (`lychee`, `security`, `codeql`) match template exactly

**`release.yml`:**

- [ ] Triggered on `v*` tags only
- [ ] `check` job — copy 1:1 from template, then replace `myapp` in the PyPI URL with app name
- [ ] `build` job — verifies tag is on main, builds sdist+wheel, attests build provenance, uploads dist artifact
- [ ] `publish-pypi` job — environment `url` uses app name (not `pypi.org/p/myapp`); uses trusted publishing with attestations
- [ ] `sbom` job — generates SPDX SBOM, attests it, uploads artifact
- [ ] `docker` job — copy 1:1 from template, then replace `myapp` in the entry-point verification step with app name. Verify the following are present and unchanged: matrix publishes to both `ghcr.io` and `docker.io`, multi-platform build (`linux/amd64`, `linux/arm64`), semver tag patterns, BuildKit provenance and SBOM (`provenance: true`, `sbom: true`), `actions/attest` build provenance attestation, Cosign keyless signing with `--recursive` and annotations (repo, workflow, ref), post-push entry-point verification (pulls by digest, runs `--help`)
- [ ] `trivy` job — calls `_trivy-image.yml` to scan the newly pushed GHCR image
- [ ] `github-release` job — creates GitHub release with dist and SBOM artifacts, `--notes-file notes.md --verify-tag` (workflow extracts changelog entry, fetches auto-generated notes via `gh api repos/.../releases/generate-notes`, combines them into notes.md); SHA256SUMS uses flat filenames (no `dist/` or `sbom/` prefixes) so `sha256sum -c` works on downloaded assets

**`docs.yml`:**

- [ ] Copy 1:1 from template — builds mkdocs with `--strict`, deploys to GitHub Pages
- [ ] Triggers on push to `main` for `docs/**`, `mkdocs.yml`, `src/**` paths + `workflow_dispatch`

**`weekly.yml`:**

- [ ] Copy 1:1 from template — runs OpenSSF Scorecard, Trivy image scan (`:latest`), security scans, CodeQL, OSV-Scanner (weekly mode) on schedule (`cron: "0 0 * * 0"`) + `workflow_dispatch`

**`labeler.yml`:**

- [ ] Copy 1:1 from template — runs `actions/labeler` on `pull_request_target` with `sync-labels: true`

### Section 6 — GitHub Config (`.github/` non-workflow)

**`settings.yml`:**

- [ ] `repository.name` uses app name (not `myapp`)
- [ ] `repository.description` updated (not still `"A CLI application. Change This"`)
- [ ] `repository.homepage` points to correct GitHub Pages URL (no `myapp`)
- [ ] `repository.topics` updated (keep `python`, `cli`, `cyclopts`; replace `change-this` with relevant topics)
- [ ] All remaining settings (merge strategy, branch protection, labels, status checks) match template exactly

**`FUNDING.yml`:**

- [ ] `github` entry uses correct owner username

**`ISSUE_TEMPLATE/bug_report.yml`:**

- [ ] Version field description references app's `--version` command (not `myapp --version`)
- [ ] Reproduction steps placeholder uses app name (not `myapp ...`)
- [ ] All remaining fields and structure match template

**`ISSUE_TEMPLATE/feature_request.yml`:**

- [ ] Copy 1:1 from template

**`PULL_REQUEST_TEMPLATE.md`:**

- [ ] Copy 1:1 from template

**`labeler.yml` (config):**

- [ ] Copy 1:1 from template — defines labels for `bug`, `feature`, `refactor`, `documentation`, `ci`, `dependencies`, `security`, `tooling` based on branch patterns and changed files

### Section 7 — Container (`Dockerfile`, `.dockerignore`)

**`Dockerfile`:**

- [ ] Copy 1:1 from template — multi-stage build (uv > builder > runtime), non-root user, cache-friendly dep install
- [ ] `ENTRYPOINT` changed to app name (not `myapp`) — only required change

**`.dockerignore`:**

- [ ] Copy 1:1 from template — excludes `.git/`, `.venv/`, tests, docs, build artifacts, config files not needed at runtime

### Section 8 — Dev Tooling & Root Config

**Copy 1:1 from template (no changes needed):**

- [ ] `justfile` — all recipes: `lint`, `lint-fix`, `typecheck`, `test`, `cov`, `complexity`, `semgrep`, `build`, `docs`, `docs-build`, `ci`, `clean`
- [ ] `.pre-commit-config.yaml` — all 9 repos: pre-commit-hooks, ruff, ty (local), validate-pyproject, complexipy, commitizen, typos, reuse, gitleaks
- [ ] `.editorconfig` — indent/charset/line-ending rules for `*`, `*.yml/yaml`, `*.json`, `*.md`
- [ ] `.gitattributes` — line-ending normalization, diff drivers, linguist overrides
- [ ] `.gitignore` — Python, dist, venv, testing, linting, type-checking, SonarCloud, docs, IDE, OS, env file patterns
- [ ] `renovate.json` — best-practices config, OSV vulnerability alerts, package rules for GHA/Dockerfile/pre-commit

**`codecov.yml`:**

- [ ] Copy 1:1 from template, then update all 3 flag `paths` entries (`unit`, `integration`, `e2e`) from `src/myapp/` to `src/<app>/`
- [ ] All remaining config (precision, range, status targets, comment layout, github_checks) unchanged

**`sonar-project.properties`:**

- [ ] `${SONAR_PROJECT_KEY}`, `${SONAR_ORG}`, `${PROJECT_NAME}` replaced with actual values
- [ ] All remaining config (python version, sources/tests paths, coverage/test report patterns, quality gate, encoding) matches template exactly

### Section 9 — Install & Local Validation

> Run everything at least once after migration — some checks may initially fail if code was ported from a different setup. The goal is to surface all issues early, then fix until everything passes.

**Environment setup:**

- [ ] `uv sync` — venv created, all deps installed
- [ ] `uv lock` — `uv.lock` generated
- [ ] `pre-commit install` — pre-commit and commit-msg hooks active

**Quality gates (via justfile):**

- [ ] `just lint` — ruff check + format
- [ ] `just lint-fix` — auto-fix lint issues if any
- [ ] `just typecheck` — ty check on src/ and tests/
- [ ] `just test` — all unit, integration, and e2e tests
- [ ] `just cov` — coverage report, must reach ≥ 70%
- [ ] `just complexity` — cognitive complexity ≤ 15
- [ ] `just semgrep` — SAST scan
- [ ] `just build` — sdist + wheel built successfully
- [ ] `just validate` — validate-pyproject passes
- [ ] `just package-check` — build + twine check + entry point smoke test
- [ ] `just docs` — mkdocs serves without errors
- [ ] `just docs-build` — mkdocs strict build passes
- [ ] `just reuse-check` — REUSE/SPDX compliance passes
- [ ] `just pre-commit` — all pre-commit hooks pass
- [ ] `just ci` — full composite gate (pre-commit + lint + typecheck + cov + complexity + semgrep + validate + docs-build + package-check + reuse-check)

**Pre-commit hooks:**

- [ ] `pre-commit run --all-files` — all hooks pass (ruff, ty, validate-pyproject, complexipy, typos, reuse, gitleaks)

### Section 10 — Global Grep Sanity Check

- [ ] `grep -r --exclude=VERIFICATION.md "myapp" .` — zero hits (template app name fully replaced)
- [ ] `grep -r --exclude=VERIFICATION.md "MYAPP_" .` — zero hits (env prefix replaced)
- [ ] `grep -r --exclude=VERIFICATION.md "Avish J\|avish.j@pm.me" .` — zero hits if author is different; expected hits if author is Avish J
- [ ] `grep -r --exclude=VERIFICATION.md "Change This\|change-this" .` — zero hits (settings.yml placeholders replaced)
- [ ] `grep -r --exclude=VERIFICATION.md "A CLI application" .` — zero hits (template description replaced)
- [ ] `grep -r --exclude=VERIFICATION.md '\${' .` — zero hits (all `${...}` placeholders like `SONAR_PROJECT_KEY`, `SONAR_ORG`, `PROJECT_NAME` resolved)
- [ ] `grep -r --exclude=VERIFICATION.md "avishj" .` — zero hits if owner is different; expected hits if owner is `avishj`

## User Scope

> Cross-reference with [SETUP.md](SETUP.md) and verify all setup steps relevant to your environment are completed. Sections 1–10 above cover file-level verification (AI scope); the items below require manual human action.

### Section 11 — Prerequisites & Local Tools

- [ ] Python 3.13+ installed and available on `PATH`
- [ ] [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- [ ] [just](https://github.com/casey/just#installation) installed
- [ ] [pre-commit](https://pre-commit.com/#install) installed
- [ ] [Docker](https://docs.docker.com/get-docker/) installed (for container builds and CI docker job)
- [ ] Git configured with commit signing (required by commitizen / sign-off workflow)

### Section 12 — GitHub Repository Setup

**Create and configure the repo:**

- [ ] Create GitHub repo — public, default branch `main`
- [ ] Go to **Settings > Pages** > set Source to **GitHub Actions**

**Add secrets** (Settings > Secrets and variables > Actions > New repository secret):

- [ ] `CODECOV_TOKEN` — get from [codecov.io](https://codecov.io) after adding the repo
- [ ] `SONAR_TOKEN` — get from [sonarcloud.io](https://sonarcloud.io) after creating the project
- [ ] `DOCKERHUB_USERNAME` — Docker Hub username (only if publishing to Docker Hub)
- [ ] `DOCKERHUB_TOKEN` — Docker Hub access token (only if publishing to Docker Hub)

**Create environment** (Settings > Environments > New environment):

- [ ] Create environment named `pypi`
- [ ] In the `pypi` environment, configure [trusted publisher](https://docs.pypi.org/trusted-publishers/) on PyPI: set repository owner, repo name, workflow `release.yml`, and environment `pypi`

**Enable security features** (Settings > Code security):

- [ ] Enable **secret scanning** with **push protection**
- [ ] Enable **Dependabot security updates** (supplements Renovate for GitHub-native security advisories)

**Enable release immutability:**

- [ ] Enable **release immutability** — Settings > scroll to "Releases" section > select "Enable release immutability" (only applies to future releases)
- [ ] Enable **Docker Hub immutable tags** — Docker Hub > Repositories > select repo > Settings > General > Tag Mutability > select "Specific tags are immutable" > set regex to `^\d+\.\d+\.\d+$` > save (protects exact semver tags while keeping `latest`, major, and major.minor tags mutable)
- [ ] **GHCR immutable tags** — not supported yet; integrity is provided by Cosign signatures and build provenance attestations in the release workflow

**Install the [Renovate GitHub App](https://github.com/apps/renovate):**

- [ ] Grant Renovate access to the repo for automated dependency updates (the `renovate.json` config is already in the template)

**First push:**

- [ ] Push to `main` and verify the CI workflow passes
- [ ] Verify docs deploy to GitHub Pages successfully
- [ ] Verify Renovate creates its onboarding PR
