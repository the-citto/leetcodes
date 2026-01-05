"""Test Add Two Numbers."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_002_add_two_numbers
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestAddTwoNumbers[*P, T](TestBase[*P, T]):
    """TestAddTwoNumbers."""

    __test__ = True

    @pytest.fixture(
        params=[
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([0], [0], [0]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_002_add_two_numbers.add_two_numbers_v1,
            lc_002_add_two_numbers.add_two_numbers_v2,
            lc_002_add_two_numbers.add_two_numbers_v3,
            lc_002_add_two_numbers.add_two_numbers_v4,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
