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

- [ ] `[dependency-groups]` `dev` contains all 11 template deps (versions may differ, none removed)

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
- [ ] Common tasks table matches template (`just lint`, `just typecheck`, etc.)
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

**`CODEOWNERS`:**

- [ ] File exists with `* @<owner>` or another valid ownership entry

### Section 5 — CI/CD Workflows (`.github/workflows/`)

**Reusable workflows (copy 1:1 from template):**

- [ ] `_codeql.yml` — CodeQL analysis with `security-and-quality` queries, paths-ignore for docs/tests, threat models configured
- [ ] `_security.yml` — Semgrep SAST, Trivy filesystem scan, Gitleaks secret scan, zizmor workflow security scan
- [ ] `_trivy-image.yml` — reusable Trivy container image scan with SARIF upload

**`ci.yml`:**

- [ ] All 13 jobs present: `lint`, `actionlint`, `docker`, `lychee`, `test`, `sonarcloud`, `package`, `complexity`, `security`, `codeql`, `dependency-review`, `markdownlint`, `ci-passed`
- [ ] `docker` job — `docker build -t` and `docker run --rm` image name uses app name (not `myapp`)
- [ ] `package` job — `uv run --with dist/*.whl --no-project --` entry-point verification uses app name (not `myapp`)
- [ ] `test` job — matrix: Python `3.13` + `3.14` (add newer versions as needed) × `ubuntu` + `macos` + `windows`; runs all 3 test tiers separately with per-tier coverage uploads to Codecov (flags: `unit`, `integration`, `e2e`)
- [ ] `ci-passed` gate job — `needs` lists all 12 other jobs
- [ ] `lint` job — ruff check, ruff format, ty check, validate-pyproject, mkdocs build --strict, typos spell check
- [ ] `sonarcloud` job — downloads test results and coverage artifacts, runs SonarCloud scan
- [ ] `complexity` job — complexipy with max-complexity 15 and SARIF upload
- [ ] `dependency-review` job — PR-only, `fail-on-severity: moderate`, license and vuln checks, SSPL/BUSL denied
- [ ] All remaining jobs (`actionlint`, `lychee`, `markdownlint`, `security`, `codeql`) match template exactly

**`release.yml`:**

- [ ] Triggered on `v*` tags only
- [ ] `build` job — verifies tag is on main, builds sdist+wheel, attests build provenance, uploads dist artifact
- [ ] `publish-pypi` job — environment `url` uses app name (not `pypi.org/p/myapp`); uses trusted publishing with attestations
- [ ] `sbom` job — generates SPDX SBOM, attests it, uploads artifact
- [ ] `docker` job — matrix publishes to both `ghcr.io` and `docker.io`; builds multi-platform (`linux/amd64`, `linux/arm64`); semver tag patterns, build provenance attestation
- [ ] `trivy` job — calls `_trivy-image.yml` to scan the newly pushed GHCR image
- [ ] `github-release` job — creates GitHub release with dist and SBOM artifacts, `--generate-notes --verify-tag`

**`docs.yml`:**

- [ ] Copy 1:1 from template — builds mkdocs with `--strict`, deploys to GitHub Pages
- [ ] Triggers on push to `main` for `docs/**`, `mkdocs.yml`, `src/**` paths + `workflow_dispatch`

**`weekly.yml`:**

- [ ] Copy 1:1 from template — runs OpenSSF Scorecard, Trivy image scan (`:latest`), security scans, CodeQL on schedule (`cron: "0 0 * * 0"`) + `workflow_dispatch`

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

- [ ] Copy 1:1 from template — multi-stage build (uv → builder → runtime), non-root user, cache-friendly dep install
- [ ] `ENTRYPOINT` changed to app name (not `myapp`) — only required change

**`.dockerignore`:**

- [ ] Copy 1:1 from template — excludes `.git/`, `.venv/`, tests, docs, build artifacts, config files not needed at runtime

### Section 8 — Dev Tooling & Root Config

### Section 9 — Install & Local Validation

## User Scope

### Section 10 — Manual GitHub Settings & Secrets
