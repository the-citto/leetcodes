"""Test Median of Two Sorted Arrays."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_004_median_of_two_sorted_arrays

if typing.TYPE_CHECKING:
    from collections.abc import Callable


params: list[tuple[list[int], list[int], float]] = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([1, 2, 3, 5], [4, 6, 7], 4.0),
    ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3.0),
    ([2, 3, 5, 8], [10, 12, 14, 16, 18, 20], 11),
    ([1, 2, 3], [], 2.0),
    ([], [1, 2, 3, 4], 2.5),
    ([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25], 11.0),
    ([23, 26, 31, 35], [3, 5, 7, 9, 11, 16], 13.5),
]


@pytest.fixture(params=params)
def data(request: pytest.FixtureRequest) -> typing.Any:
    """Longest Substring Without Repeating Characters data."""
    return request.param


@pytest.fixture(
    params=[
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v1,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v2,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v3,
        lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v4,
    ],
    ids=lambda p: p.__name__.replace("median_of_two_sorted_arrays_", ""),
)
def func(request: pytest.FixtureRequest) -> typing.Any:
    """Longest Substring Without Repeating Characters function."""
    return request.param


def test_median_of_two_sorted_arrays(
    func: Callable[[list[int], list[int]], float],
    data: tuple[list[int], list[int], float],
) -> None:
    """Test Longest Substring Without Repeating Characters."""
    nums1, nums2, expected = data
    assert func(nums1, nums2) == expected
