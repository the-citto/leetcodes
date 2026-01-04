"""Test Longest Palindromic Substring."""

# from __future__ import annotations
#
# import typing
#
# import pytest
#
# from leetcodes import lc_005_long_palindr_substr
#
# if typing.TYPE_CHECKING:
#     from collections.abc import Callable
#
#
# params: list[tuple[str, str]] = [
#     ("babad", "bab"),
#     ("cbbd", "bb"),
#     ("", ""),
#     ("a", "a"),
#     ("123454321a12345", "54321a12345"),
# ]
#
#
# @pytest.fixture(params=params)
# def data(request: pytest.FixtureRequest) -> typing.Any:
#     """Return data."""
#     return request.param
#
#
# @pytest.fixture(
#     params=[
#         lc_005_long_palindr_substr.long_palindr_substr_v1,
#         lc_005_long_palindr_substr.long_palindr_substr_v2,
#     ],
#     ids=lambda p: p,
# )
# def func(request: pytest.FixtureRequest) -> typing.Any:
#     """Return function."""
#     return request.param
#
#
# def test_lc_005(
#     func: Callable[[str], str],
#     data: tuple[str, str],
# ) -> None:
#     """Test Longest Palindromic Substring."""
#     s, expected = data
#     assert func(s) == expected
