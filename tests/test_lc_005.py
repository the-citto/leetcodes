"""Test Longest Palindromic Substring."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_005_long_palindr_substr
from tests.test_base import TestBase

if typing.TYPE_CHECKING:
    from collections.abc import Callable


class TestLongestPalindromicSubstring[*P, T](TestBase[*P, T]):
    """TestLongestPalindromicSubstring."""

    __test__ = True

    @pytest.fixture(
        params=[
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("", ""),
            ("a", "a"),
            ("123454321a12345", "54321a12345"),
            ("abaxabaxabyybaxabyb", "baxabyybaxab"),
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
        ids=lambda p: p.__name__.split("_")[-1],
    )
    def func(self, request: pytest.FixtureRequest) -> typing.Any:
        """Return function."""
        return request.param

    @typing.override
    def test_run(self, func: Callable[[*P], T], data: tuple[*P, T]) -> None:
        super().test_run(func, data)
