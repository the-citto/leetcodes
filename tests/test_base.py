"""Test base."""

from __future__ import annotations

import abc
import typing

import pytest

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestBase[*P, T](abc.ABC):
    """TestBase."""

    __test__ = False

    @pytest.fixture
    @abc.abstractmethod
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""

    @pytest.fixture
    @abc.abstractmethod
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""

    @abc.abstractmethod
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        """The standard test execution logic."""
        expected = data[-1]
        args = data[:-1]
        assert func(*args) == expected
