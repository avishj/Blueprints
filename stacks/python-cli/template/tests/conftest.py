"""Shared test fixtures."""

from collections.abc import Callable

import pytest

from myapp.cli import app


class CliResult:
    """Captures exit code and stdout from a cyclopts app invocation."""

    def __init__(self, exit_code: int, output: str) -> None:
        self.exit_code = exit_code
        self.output = output


@pytest.fixture
def invoke(capsys: pytest.CaptureFixture[str]) -> Callable[..., CliResult]:
    """Invoke the CLI app and return a result with exit_code and output."""
    def _invoke(*args: str) -> CliResult:
        try:
            app.meta(list(args))
            captured = capsys.readouterr()
            return CliResult(exit_code=0, output=captured.out)
        except SystemExit as exc:
            captured = capsys.readouterr()
            return CliResult(exit_code=exc.code or 0, output=captured.out)
    return _invoke
