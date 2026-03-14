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

### Section 5 — CI/CD Workflows (`.github/workflows/`)

### Section 6 — GitHub Config (`.github/` non-workflow)

### Section 7 — Container (`Dockerfile`, `.dockerignore`)

### Section 8 — Dev Tooling & Root Config

### Section 9 — Install & Local Validation

## User Scope

### Section 10 — Manual GitHub Settings & Secrets
