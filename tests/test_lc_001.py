"""Test Two Sum."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_001_two_sum
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestTwoSum[*P, T](TestBase[*P, T]):
    """TestTwoSum."""

    __test__ = True

    @pytest.fixture(
        params=[
            typing.cast("tuple[*P, T]", ([], 0, [])),
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5, 5], 10, [4, 5]),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_001_two_sum.two_sum_v1,
            lc_001_two_sum.two_sum_v2,
            lc_001_two_sum.two_sum_v3,
            lc_001_two_sum.two_sum_v4,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
