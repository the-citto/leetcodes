"""5. Longest Palindromic Substring.

URL:
    https://leetcode.com/problems/longest-palindromic-substring
"""

from __future__ import annotations


def long_palindr_substr_v1(s: str) -> str:
    """Longest Palindromic Substring."""
    len_s = len(s)
    out = ""
    for i in range(len_s):
        for j in range(len(s[i:])):
            candidate = s[i : j + i + 1]
            if candidate == candidate[::-1] and len(candidate) > len(out):
                out = candidate
    return out


def long_palindr_substr_v2(s: str) -> str:
    """Longest Palindromic Substring.

    Manacher's algorithm.
    """
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    radius_array = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        if i < right:
            radius_array[i] = min(right - i, radius_array[2 * center - i])
        while t[i + radius_array[i] + 1] == t[i - radius_array[i] - 1]:
            radius_array[i] += 1
        if i + radius_array[i] > right:
            center, right = i, i + radius_array[i]
    center_index, max_len = max(enumerate(radius_array), key=lambda x: x[1])
    start = (center_index - max_len) // 2
    return s[start : start + max_len]
