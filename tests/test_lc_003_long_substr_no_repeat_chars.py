"""Test Longest Substring Without Repeating Characters."""

from __future__ import annotations

import typing

import pytest

from leetcodes import lc_003_long_substr_no_repeat_chars

if typing.TYPE_CHECKING:
    from collections.abc import Callable


params: list[tuple[str, int]] = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.fixture(params=params)
def data(request: pytest.FixtureRequest) -> typing.Any:
    """Longest Substring Without Repeating Characters data."""
    return request.param


@pytest.fixture(
    params=[
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v1,
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v2,
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v3,
    ],
    ids=lambda p: p.__name__.replace("long_substr_no_repeat_chars_", ""),
)
def func(request: pytest.FixtureRequest) -> typing.Any:
    """Longest Substring Without Repeating Characters function."""
    return request.param


def test_long_substr_no_repeat_chars(
    func: Callable[[str], int],
    data: tuple[str, int],
) -> None:
    """Test Longest Substring Without Repeating Characters."""
    s, expected = data
    assert func(s) == expected
