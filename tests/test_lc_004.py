"""Test Median of Two Sorted Arrays."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_004_median_of_two_sorted_arrays
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestMedianOfTwoSortedArrays[*P, T](TestBase[*P, T]):
    """TestMedianOfTwoSortedArrays."""

    __test__ = True

    @pytest.fixture(
        params=[
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([1, 2, 3, 5], [4, 6, 7], 4.0),
            ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3.0),
            ([2, 3, 5, 8], [10, 12, 14, 16, 18, 20], 11),
            typing.cast("tuple[*P, T]", ([1, 2, 3], [], 2.0)),
            typing.cast("tuple[*P, T]", ([], [1, 2, 3, 4], 2.5)),
            typing.cast("tuple[*P, T]", ([], [], 0.0)),
            ([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25], 11.0),
            ([23, 26, 31, 35], [3, 5, 7, 9, 11, 16], 13.5),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v1,
            lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v2,
            lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v3,
            lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v4,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
