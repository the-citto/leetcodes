"""4. Median of Two Sorted Arrays.

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively,
return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""

UPPER_BOUND = 1 << 21
LOWER_BOUND = -UPPER_BOUND


def median_of_two_sorted_arrays_v1(nums1: list[int], nums2: list[int]) -> float:
    """Median of Two Sorted Arrays."""
    nums = sorted([*nums1, *nums2])
    len_nums = len(nums)
    mid_id = len_nums // 2
    mid_num = nums[mid_id]
    if len_nums % 2:
        return float(mid_num)
    return (mid_num + nums[mid_id - 1]) / 2


def median_of_two_sorted_arrays_v2(nums1: list[int], nums2: list[int]) -> float:
    """Median of Two Sorted Arrays."""
    nums = sorted([*nums1, *nums2])
    len_nums = len(nums)
    nums_dict = dict(zip(range(len_nums), nums, strict=True))
    mid_id = len_nums // 2
    mid_num = nums_dict[mid_id]
    if len_nums % 2:
        return float(mid_num)
    return (mid_num + nums_dict[mid_id - 1]) / 2


def median_of_two_sorted_arrays_v3(nums1: list[int], nums2: list[int]) -> float:
    """Median of Two Sorted Arrays."""
    x_nums, y_nums = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    x_len = len(x_nums)
    y_len = len(y_nums)
    start = 0
    end = len(x_nums)
    while True:
        x_id = (end + start) // 2
        y_id = (x_len + y_len + 1) // 2 - x_id
        x_left = x_nums[:x_id] or [LOWER_BOUND]
        x_right = x_nums[x_id:] or [UPPER_BOUND]
        y_left = y_nums[:y_id] or [LOWER_BOUND]
        y_right = y_nums[y_id:] or [UPPER_BOUND]
        if x_left[-1] <= y_right[0] and y_left[-1] <= x_right[0]:
            max_left = max(x_left[-1], y_left[-1])
            if (x_len + y_len) % 2:
                return float(max_left)
            return (max_left + min(x_right[0], y_right[0])) / 2
        if x_left[-1] <= y_right[0]:
            start = x_id + 1
        else:
            end = x_id - 1


def median_of_two_sorted_arrays_v4(nums1: list[int], nums2: list[int]) -> float:
    """Median of Two Sorted Arrays."""
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    len1 = len(nums1)
    len2 = len(nums2)
    start = 0
    end = len1
    total_half = (len1 + len2 + 1) // 2
    while start <= end:
        id1 = (start + end) // 2
        id2 = total_half - id1
        left1 = nums1[id1 - 1] if id1 > 0 else LOWER_BOUND
        right1 = nums1[id1] if id1 < len1 else UPPER_BOUND
        left2 = nums2[id2 - 1] if id2 > 0 else LOWER_BOUND
        right2 = nums2[id2] if id2 < len2 else UPPER_BOUND
        if left1 <= right2 and left2 <= right1:
            max_left = max(left1, left2)
            if (len1 + len2) % 2:
                return float(max_left)
            return (max_left + min(right1, right2)) / 2
        if left1 <= right2:
            start = id1 + 1
        else:
            end = id1 - 1
    return 0.0
