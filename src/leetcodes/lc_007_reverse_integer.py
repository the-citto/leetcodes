"""7. Reverse Integer.

URL:
    https://leetcode.com/problems/reverse-integer
"""

from __future__ import annotations

import math


def reverse_integer_v1(x: int) -> int:
    """Reverse Integer."""
    max_int = 2**31 - 1
    min_int = -(2**31)
    max_discriminant = 7
    min_discriminant = -8
    max_threshold = max_int // 10
    min_threshold = int(min_int / 10)
    res = 0
    while x != 0:
        pop = int(math.fmod(x, 10))
        x = int(x / 10)
        if res > max_threshold or (res == max_threshold and pop > max_discriminant):
            return 0
        if res < min_threshold or (res == min_threshold and pop < min_discriminant):
            return 0
        res = (res * 10) + pop
    return res


def reverse_integer_v2(x: int) -> int:
    """Reverse Integer."""
    is_negative = x < 0
    max_int = 2**31 - 1
    min_int = -(2**31)
    max_threshold = max_int // 10
    min_threshold = int(min_int / 10)
    max_discriminant = 7
    min_discriminant = -8
    res = 0
    while x != 0:
        pop = x % 10
        if is_negative:
            pop -= 10
        x = int(x / 10)
        if res > max_threshold or (res == max_threshold and pop > max_discriminant):
            return 0
        if res < min_threshold or (res == min_threshold and pop < min_discriminant):
            return 0
        res = (res * 10) + pop
    return res


# C++ without python cheats
# int reverse(int x) {
#     int res = 0;
#     while (x != 0) {
#         int pop = x % 10;
#         x /= 10;
#         if (res > INT_MAX/10 || (res == INT_MAX / 10 && pop > 7)) return 0;
#         if (res < INT_MIN/10 || (res == INT_MIN / 10 && pop < -8)) return 0;
#         res = res * 10 + pop;
#     }
#     return res;
# }
