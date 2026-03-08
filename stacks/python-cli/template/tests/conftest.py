"""Shared test fixtures."""

from collections.abc import Callable

import pytest
from typer.testing import CliRunner, Result

from myapp.cli import app


@pytest.fixture
def runner() -> CliRunner:
    """Create a CLI test runner."""
    return CliRunner()


@pytest.fixture
def invoke(runner: CliRunner) -> Callable[..., Result]:
    """Invoke the CLI app."""
    def _invoke(*args: str) -> Result:
        return runner.invoke(app, list(args))
    return _invoke
