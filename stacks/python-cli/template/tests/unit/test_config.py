"""Unit tests for application configuration."""

import pytest

from myapp.config import Settings


pytestmark = pytest.mark.unit


def test_defaults():
    s = Settings()
    assert s.debug is False
    assert s.verbose is False


def test_env_prefix(monkeypatch):
    monkeypatch.setenv("MYAPP_DEBUG", "true")
    monkeypatch.setenv("MYAPP_VERBOSE", "1")
    s = Settings()
    assert s.debug is True
    assert s.verbose is True


def test_env_without_prefix_ignored(monkeypatch):
    monkeypatch.setenv("DEBUG", "true")
    s = Settings()
    assert s.debug is False
