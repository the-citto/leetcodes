"""Test leetcodes."""

from __future__ import annotations

import typing

import pytest

from leetcodes import (
    lc_001_two_sum,
    lc_002_add_two_numbers,
    lc_003_long_substr_no_repeat_chars,
    lc_004_median_of_two_sorted_arrays,
    lc_005_long_palindr_substr,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestLc001TwoSum:
    """TestLc001TwoSum."""

    @pytest.fixture(
        params=[
            typing.cast("tuple[list[int], int, list[int]]", ([], 0, [])),
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

    def test_run(self, func: Callable[[list[int], int], list[int]], data: tuple[list[int], int, list[int]]) -> None:
        """Test run."""
        nums, target, expected = data
        assert func(nums, target) == expected


class TestLc002AddTwoNumbers:
    """TestLc002AddTwoNumbers."""

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

    def test_run(
        self,
        func: Callable[[list[int], list[int]], list[int]],
        data: tuple[list[int], list[int], list[int]],
    ) -> None:
        """Test run."""
        l1, l2, expected = data
        assert func(l1, l2) == expected


class TestLc003LongestSubstringWithoutRepeatingCharacters:
    """TestLc003LongestSubstringWithoutRepeatingCharacters."""

    @pytest.fixture(
        params=[
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v1,
            lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v2,
            lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v3,
        ],
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    def test_run(self, func: Callable[[str], int], data: tuple[str, int]) -> None:
        """Test run."""
        s, expected = data
        assert func(s) == expected


class TestLc004MedianOfTwoSortedArrays:
    """TestLc004MedianOfTwoSortedArrays."""

    @pytest.fixture(
        params=[
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([1, 2, 3, 5], [4, 6, 7], 4.0),
            ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3.0),
            ([2, 3, 5, 8], [10, 12, 14, 16, 18, 20], 11),
            typing.cast("tuple[list[int], list[int], float]", ([1, 2, 3], [], 2.0)),
            typing.cast("tuple[list[int], list[int], float]", ([], [1, 2, 3, 4], 2.5)),
            typing.cast("tuple[list[int], list[int], float]", ([], [], 0.0)),
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

    def test_run(self, func: Callable[[list[int], list[int]], float], data: tuple[list[int], list[int], float]) -> None:
        """Test run."""
        nums1, nums2, expected = data
        assert func(nums1, nums2) == expected


class TestLc005LongestPalindromicSubstring:
    """TestLc005LongestPalindromicSubstring."""

    @pytest.fixture(
        params=[
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("", ""),
            ("a", "a"),
            ("123454321a12345", "54321a12345"),
        ],
    )
    def data(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return data."""
        return request.param

    @pytest.fixture(
        params=[
            lc_005_long_palindr_substr.long_palindr_substr_v1,
            lc_005_long_palindr_substr.long_palindr_substr_v2,
        ],
        ids=lambda p: p,
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    def test_run(self, func: Callable[[str], str], data: tuple[str, str]) -> None:
        """Test run."""
        s, expected = data
        assert func(s) == expected
