"""1. Two Sum.

URL:
    https://leetcode.com/problems/two-sum
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
