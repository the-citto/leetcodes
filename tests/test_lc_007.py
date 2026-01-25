"""Test Reverse Integer."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_007_reverse_integer
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestReverseInteger[*P, T](TestBase[*P, T]):
    """TestReverseInteger."""

    __test__ = True

    @pytest.fixture(
        params=[
            (123, 321),
            (-123, -321),
            (7463847412, 2147483647),
            (-8463847412, -2147483648),
            (2147483648, 0),
            (-2147483649, 0),
            (5, 5),
            (-5, -5),
            (0, 0),
            (1200, 21),
            (10, 1),
            (1463847412, 2147483641),
            (1000000003, 0),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_007_reverse_integer.reverse_integer_v1,
            lc_007_reverse_integer.reverse_integer_v2,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
