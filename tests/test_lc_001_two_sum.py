"""Test Two Sum."""

from __future__ import annotations

import typing

import pytest

from leetcodes.lc_001_two_sum import (
    two_sum_v1,
    two_sum_v2,
    two_sum_v3,
    two_sum_v4,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable


params: list[tuple[list[int], int, list[int]]] = [
    ([], 0, []),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3, 4, 5, 5], 10, [4, 5]),
]


@pytest.fixture(params=params)
def data(request: pytest.FixtureRequest) -> typing.Any:
    """Two sum data."""
    return request.param


@pytest.fixture(
    params=[
        two_sum_v1,
        two_sum_v2,
        two_sum_v3,
        two_sum_v4,
    ],
    ids=["v1", "v2", "v3", "v4"],
)
def func(request: pytest.FixtureRequest) -> typing.Any:
    """Two Sum function."""
    return request.param


def test_two_sum_v1(func: Callable[[list[int], int], list[int]], data: tuple[list[int], int, list[int]]) -> None:
    """Test Two Sum."""
    nums, target, expected = data
    assert func(nums, target) == expected
