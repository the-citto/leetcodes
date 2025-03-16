"""1. Two Sum.

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]


Constraints:
    2 <= nums.length <= 10**4
    -10**9 <= nums[i] <= 10**9
    -10**9 <= target <= 10**9
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


MIN_ARRAY_LEN = 2
MAX_ARRAY_LEN = 10**4
MIN_VALUE = -10**9
MAX_VALUE = 10**9


class ConstraintError(ValueError):
    """Constraint error."""


def _check_constraint(nums: list[int], target: int) -> None:
    nums_len = len(nums)
    if nums_len < MIN_ARRAY_LEN or nums_len > MAX_ARRAY_LEN:
        err_msg = (
            f"The number of elements in 'nums' should be >= {MIN_ARRAY_LEN} and <= {MAX_ARRAY_LEN:.1E}. "
            f"Length of 'nums' = {nums_len:,}"
        )
        raise ConstraintError(err_msg)
    if not MIN_VALUE <= target <= MAX_VALUE:
        err_msg = (
            f"The value of 'target' should be >= {MIN_VALUE:.1E} and <= {MAX_VALUE:.1E}. "
            f"'target' = {target:,}"
        )
        raise ConstraintError(err_msg)
    if min(nums) < MIN_VALUE:
        err_msg = (
            f"The values of 'nums' should be >= {MIN_VALUE:.1E}. "
            f"Found {min(nums):,}"
        )
        raise ConstraintError(err_msg)
    if max(nums) > MAX_VALUE:
        err_msg = (
            f"The values of 'nums' should be <= {MAX_VALUE:.1E}. "
            f"Found {max(nums):,}"
        )
        raise ConstraintError(err_msg)


def two_sum(nums: list[int], target: int) -> list[int]:
    """Solve."""
    _check_constraint(nums=nums, target=target)
    while nums:
        num_1 = nums.pop()
        num_2_lst = [n for n in nums if n + num_1 == target]
        if num_2_lst:
            if len(num_2_lst) > 1:
                err_msg = f"Found two valid answers: {num_1}, '{num_2_lst}'"
                raise ConstraintError(err_msg)
            return [num_1, num_2_lst[0]]
    err_msg = "No values found."
    raise ValueError(err_msg)





