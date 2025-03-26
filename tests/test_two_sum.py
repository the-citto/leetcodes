"""Test two_sum."""

import pytest

from leetcode.two_sum import (
    MAX_ARRAY_LEN,
    MAX_VALUE,
    MIN_VALUE,
    ConstraintError,
    two_sum_eafp,
)


CORRECT = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]
CONSTRAINTS = [
    ([], 1),
    ([1], 1),
    ([1] * (MAX_ARRAY_LEN + 1) , 1),
    ([1, MIN_VALUE - 1], 1),
    ([1, MAX_VALUE + 1], 1),
    ([1, 2], MIN_VALUE - 1),
    ([1, 2], MAX_VALUE + 1),
]
MULTI_RESULTS = [
    ([1, 2, 2], 3),
]
NO_RESULT = [
    ([1, 2], 4),
]



@pytest.mark.parametrize(("nums", "target", "expected"), CORRECT)
def test_correct(nums: list[int], target: int, expected: list[int]) -> None:
    """Test correct."""
    assert two_sum_eafp(nums=nums, target=target) == expected


@pytest.mark.parametrize(("nums", "target"), CONSTRAINTS)
def test_error_constraints(nums: list[int], target: int) -> None:
    """Test constraints."""
    with pytest.raises(ConstraintError):
        two_sum_eafp(nums=nums, target=target)


@pytest.mark.parametrize(("nums", "target"), MULTI_RESULTS)
def test_error_multi_results(nums: list[int], target: int) -> None:
    """Test constraints."""
    with pytest.raises(ConstraintError):
        two_sum_eafp(nums=nums, target=target)


@pytest.mark.parametrize(("nums", "target"), NO_RESULT)
def test_error_no_result(nums: list[int], target: int) -> None:
    """Test constraints."""
    with pytest.raises(ConstraintError):
        two_sum_eafp(nums=nums, target=target)






#
# def two_sum_eafp(nums: list[int], target: int) -> list[int]:
#     """Solve."""
#     _check_constraint(nums=nums, target=target)
#     while nums:
#         num_1 = nums.pop(0)
#         num_2_lst = [n for n in nums if n + num_1 == target]
#         if num_2_lst:
#             if len(num_2_lst) > 1:
#                 err_msg = f"Found two valid answers: {num_1}, '{num_2_lst}'"
#                 raise ConstraintError(err_msg)
#             return [num_1, num_2_lst[0]]
#     err_msg = "No values found."
#     raise ValueError(err_msg)






