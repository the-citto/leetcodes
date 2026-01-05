"""Test Longest Substring Without Repeating Characters."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_003_long_substr_no_repeat_chars
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestLongestSubstringWithoutRepeatingCharacters[*P, T](TestBase[*P, T]):
    """TestAddTwoNumbers."""

    __test__ = True

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

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
