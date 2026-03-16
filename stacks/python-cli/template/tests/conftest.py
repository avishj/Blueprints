# SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Shared test fixtures."""

from collections.abc import Callable
from typing import NamedTuple

import pytest

from myapp.cli import app


class CliResult(NamedTuple):
    """Captures exit code and stdout from a cyclopts app invocation."""

    exit_code: int
    output: str


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
            code = exc.code if isinstance(exc.code, int) else (0 if exc.code is None else 1)
            return CliResult(exit_code=code, output=captured.out)
    return _invoke
