"""Test two_sum."""

import pytest

from leetcode.two_sum import two_sum


CORRECT_CASES = [
    ([2, 7, 11, 15], 9, [2, 7]),
    ([3, 2, 4], 6, [2, 4]),
    ([3, 3], 6, [3, 3]),
]



@pytest.mark.parametrize(("nums", "target", "expected"), CORRECT_CASES)
def test_correct(nums: list[int], target: int, expected: list[int]) -> None:
    """Test correct."""
    assert sorted(two_sum(nums=nums, target=target)) == sorted(expected)



    # @pytest.mark.parametrize(("el", "order"), field_sigle_values)
    # def test_init_valid(self, el: int, order: int) -> None:





