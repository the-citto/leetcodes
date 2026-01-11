"""5. Longest Palindromic Substring.

Given a string `s`, return _the longest palindromic substring_ in `s`.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
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


def long_palindr_substr_v3(s: str) -> str:
    """Longest Palindromic Substring.

    Suffix Tree, Ukkonen's algorithm.
    """
    return s


# dev
