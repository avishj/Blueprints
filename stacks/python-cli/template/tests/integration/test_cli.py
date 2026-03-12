"""CLI integration tests."""

import pytest

from myapp import __version__


pytestmark = pytest.mark.integration


def test_version(invoke):
    result = invoke("--version")
    assert result.exit_code == 0
    assert __version__ in result.output


def test_hello(invoke):
    result = invoke("hello", "World")
    assert result.exit_code == 0
    assert "World" in result.output


def test_no_args(invoke):
    result = invoke()
    assert result.exit_code == 0
    assert "Usage" in result.output
