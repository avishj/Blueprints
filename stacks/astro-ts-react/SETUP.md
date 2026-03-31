# Setup

## Prerequisites

- [ ] Bun installed
- [ ] Copier available (`uvx copier`)

## Scaffold (interactive)

```bash
git clone https://github.com/avishj/blueprints /tmp/blueprints
uvx copier copy /tmp/blueprints/stacks/astro-ts-react my-project --trust
rm -rf /tmp/blueprints
```

Copier will prompt for:

| Variable | Description | Example |
|---|---|---|
| `project_name` | Project/package name | `my-app` |
| `owner` | GitHub owner | `avishj` |
| `description` | One-line summary | `A modern Astro + React app.` |
| `author_name` | Author display name | `Avish J` |
| `author_email` | Author email | `avish.j@pm.me` |
| `copyright_year` | Copyright year | `2026` |
| `env_prefix` | Environment prefix (derived) | `MY_APP_` |

## Locked defaults (not user-prompts)

- Runtime is locked to Bun (`runtime=bun`).
- TypeScript strict mode is locked on (`strict_typescript=true`).

These are intentional stack constraints and validated by the template.

## Derived variables

- `package_name` is derived from `project_name` (lowercased).
- `module_name` is derived from `project_name` (hyphens replaced with underscores).
- `env_prefix` defaults to `{{ module_name | upper }}_` and can be overridden.

## Scaffold (non-interactive)

```bash
git clone https://github.com/avishj/blueprints /tmp/blueprints
uvx copier copy /tmp/blueprints/stacks/astro-ts-react my-project \
  --trust \
  --data project_name=my-app \
  --data owner=avishj \
  --data description="A modern Astro + React app." \
  --data author_name="Avish J" \
  --data author_email="avish.j@pm.me" \
  --data copyright_year="2026"
rm -rf /tmp/blueprints
```
