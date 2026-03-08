"""Unit tests for application configuration."""

import pytest

from myapp.config import Settings


pytestmark = pytest.mark.unit


def test_defaults(monkeypatch):
    monkeypatch.delenv("MYAPP_DEBUG", raising=False)
    monkeypatch.delenv("MYAPP_VERBOSE", raising=False)
    s = Settings(_env_file=None)
    assert s.debug is False
    assert s.verbose is False


def test_env_prefix(monkeypatch):
    monkeypatch.setenv("MYAPP_DEBUG", "true")
    monkeypatch.setenv("MYAPP_VERBOSE", "1")
    s = Settings(_env_file=None)
    assert s.debug is True
    assert s.verbose is True


def test_env_without_prefix_ignored(monkeypatch):
    monkeypatch.delenv("MYAPP_DEBUG", raising=False)
    monkeypatch.setenv("DEBUG", "true")
    s = Settings(_env_file=None)
    assert s.debug is False
