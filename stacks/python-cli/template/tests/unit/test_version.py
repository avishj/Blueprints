# SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for package metadata."""

import pytest

from myapp import __version__


pytestmark = pytest.mark.unit


def test_version_is_string():
    assert isinstance(__version__, str)


def test_version_is_semver():
    parts = __version__.split(".")
    assert len(parts) == 3
    assert all(p.isdigit() for p in parts)
