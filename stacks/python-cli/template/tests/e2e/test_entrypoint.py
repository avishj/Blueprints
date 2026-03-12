"""End-to-end tests invoking the CLI as a subprocess."""

import subprocess

import pytest


pytestmark = pytest.mark.e2e


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["myapp", *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_version_flag():
    result = _run("--version")
    assert result.returncode == 0
    assert result.stdout.strip()


def test_hello_command():
    result = _run("hello", "World")
    assert result.returncode == 0
    assert "World" in result.stdout


def test_no_args_shows_help():
    result = _run()
    assert result.returncode == 0
    assert "Usage" in result.stdout or "myapp" in result.stdout


def test_invalid_command():
    result = _run("nonexistent")
    assert result.returncode != 0
