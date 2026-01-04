"""1. Two Sum.

Given an array of integers `nums` and an integer `target`, return
_indices of the two numbers such that they add up to_ `target`.

You may assume that each input would have **_exactly_ one solution**, and you may not
use the _same_ element twice.

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
    `2 <= nums.length <= 10**4`
    -10**9 <= nums[i] <= 10**9``
    -10**9 <= target <= 10**9``
    **Only one valid answer exists.**


Follow-up: Can you come up with an algorithm that is less than O(n**2) time complexity?
"""

from __future__ import annotations

import contextlib


def two_sum_v1(nums: list[int], target: int) -> list[int]:
    """Two sum N^2."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_v2(nums: list[int], target: int) -> list[int]:
    """Two sum N^2 C."""
    for i, num in enumerate(nums):
        with contextlib.suppress(ValueError):
            j = nums[i + 1 :].index(target - num)
            return [i, j + i + 1]
    return []


def two_sum_v3(nums: list[int], target: int) -> list[int]:
    """Two sum N."""
    nums_dict = {num: i for i, num in enumerate(nums)}
    for first_id, num in enumerate(nums):
        second_num = target - num
        if second_num in nums_dict and nums_dict[second_num] != first_id:
            return [first_id, nums_dict[second_num]]
    return []


def two_sum_v4(nums: list[int], target: int) -> list[int]:
    """Two sum N C."""
    nums_dict = {num: i for i, num in enumerate(nums)}
    out = [
        [first_id, nums_dict[target - num]]
        for first_id, num in enumerate(nums)
        if (target - num) in nums_dict and nums_dict[target - num] != first_id
    ]
    if out:
        return out[0]
    return []
