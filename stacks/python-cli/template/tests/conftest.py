"""Shared test fixtures."""

import pytest
from typer.testing import CliRunner

from myapp.cli import app


@pytest.fixture
def runner() -> CliRunner:
    """Create a CLI test runner."""
    return CliRunner()


@pytest.fixture
def invoke(runner: CliRunner):
    """Invoke the CLI app."""
    def _invoke(*args: str):
        return runner.invoke(app, list(args))
    return _invoke
