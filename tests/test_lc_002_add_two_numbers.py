"""Test Add Two Numbers."""

# from __future__ import annotations
#
# import typing
#
# import pytest
#
# from leetcodes import lc_002_add_two_numbers
#
# if typing.TYPE_CHECKING:
#     from collections.abc import Callable
#
#
# params: list[tuple[list[int], list[int], list[int]]] = [
#     ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
#     ([0], [0], [0]),
#     ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
# ]
#
#
# @pytest.fixture(params=params)
# def data(request: pytest.FixtureRequest) -> typing.Any:
#     """Add two numbers data."""
#     return request.param
#
#
# @pytest.fixture(
#     params=[
#         lc_002_add_two_numbers.add_two_numbers_v1,
#         lc_002_add_two_numbers.add_two_numbers_v2,
#         lc_002_add_two_numbers.add_two_numbers_v3,
#         lc_002_add_two_numbers.add_two_numbers_v4,
#     ],
#     ids=lambda p: p,
# )
# def func(request: pytest.FixtureRequest) -> typing.Any:
#     """Add Two Numbers function."""
#     return request.param
#
#
# def test_lc_002(
#     func: Callable[[list[int], list[int]], list[int]],
#     data: tuple[list[int], list[int], list[int]],
# ) -> None:
#     """Test Add Two Numbers."""
#     l1, l2, expected = data
#     assert func(l1, l2) == expected
