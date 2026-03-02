# myapp

[![CI](https://github.com/username/myapp/actions/workflows/ci.yml/badge.svg)](https://github.com/username/myapp/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/username/myapp/branch/main/graph/badge.svg)](https://codecov.io/gh/username/myapp)
[![PyPI](https://img.shields.io/pypi/v/myapp)](https://pypi.org/project/myapp/)
[![Python](https://img.shields.io/pypi/pyversions/myapp)](https://pypi.org/project/myapp/)
[![License](https://img.shields.io/github/license/username/myapp)](LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/username/myapp/badge)](https://scorecard.dev/viewer/?uri=github.com/username/myapp)

A CLI application.

## Installation

```bash
uv tool install myapp
```

Or with pip:

```bash
pip install myapp
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
git clone https://github.com/username/myapp.git
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

## Documentation

[https://username.github.io/myapp](https://username.github.io/myapp)

## License

[AGPL-3.0-or-later](LICENSE)
