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

### Section 3 — Tests

### Section 4 — Docs & Community

### Section 5 — CI/CD Workflows (`.github/workflows/`)

### Section 6 — GitHub Config (`.github/` non-workflow)

### Section 7 — Container (`Dockerfile`, `.dockerignore`)

### Section 8 — Dev Tooling & Root Config

### Section 9 — Install & Local Validation

## User Scope

### Section 10 — Manual GitHub Settings & Secrets
