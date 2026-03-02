# myapp

[![CI](https://github.com/avishj/myapp/actions/workflows/ci.yml/badge.svg)](https://github.com/avishj/myapp/actions/workflows/ci.yml)
[![CodeQL](https://github.com/avishj/myapp/actions/workflows/codeql.yml/badge.svg)](https://github.com/avishj/myapp/actions/workflows/codeql.yml)
[![codecov](https://codecov.io/gh/avishj/myapp/branch/main/graph/badge.svg)](https://codecov.io/gh/avishj/myapp)
[![PyPI](https://img.shields.io/pypi/v/myapp)](https://pypi.org/project/myapp/)
[![Downloads](https://img.shields.io/pypi/dm/myapp)](https://pypi.org/project/myapp/)
[![Python](https://img.shields.io/pypi/pyversions/myapp)](https://pypi.org/project/myapp/)
[![License](https://img.shields.io/github/license/avishj/myapp)](LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/avishj/myapp/badge)](https://scorecard.dev/viewer/?uri=github.com/avishj/myapp)
[![Docker](https://img.shields.io/docker/v/avishj/myapp?label=docker)](https://hub.docker.com/r/avishj/myapp)

A CLI application.

## Features

- Subcommand based CLI built with [Typer](https://typer.tiangolo.com/)
- Rich terminal output via [Rich](https://rich.readthedocs.io/)
- Typed configuration from environment variables and `.env` files via [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- Fully typed with [PEP 561](https://peps.python.org/pep-0561/) `py.typed` marker
- Python 3.13+ support

## Installation

```bash
uv tool install myapp
```

Or with pip:

```bash
pip install myapp
```

Or with Docker:

```bash
docker run --rm ghcr.io/avishj/myapp --help
```

## Usage

```bash
myapp --help
myapp hello World
```

## Development

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)

### Setup

```bash
git clone https://github.com/avishj/myapp.git
cd myapp
uv sync
pre-commit install
```

### Common tasks

```bash
just lint        # lint and format check
just typecheck   # run type checker
just test        # run tests
just cov         # run tests with coverage
just ci          # run all quality gates
just docs        # serve docs locally
just clean       # remove build artifacts
```

## Configuration

myapp reads configuration from environment variables prefixed with `MYAPP_` and from `.env` files.

| Variable | Default | Description |
| --- | --- | --- |
| `MYAPP_DEBUG` | `false` | Enable debug mode |
| `MYAPP_VERBOSE` | `false` | Enable verbose output |

## Documentation

[https://avishj.github.io/myapp](https://avishj.github.io/myapp)

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make your changes and run `just ci` to verify
4. Commit using [conventional commits](https://www.conventionalcommits.org/)
5. Open a pull request

## License

[AGPL-3.0-or-later](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=avishj/myapp&type=Date)](https://star-history.com/#avishj/myapp&Date)
