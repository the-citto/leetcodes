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
    """Longest Palindromic Substring."""
    len_s = len(s)
    out = ""
    for i in range(len_s):
        for j in range(len(s[i:])):
            candidate = s[i : j + i + 1]
            if candidate == candidate[::-1] and len(candidate) > len(out):
                out = candidate
    return out


# def long_palindr_substr_v3(s: str) -> str:
#     """Longest Palindromic Substring."""
#     # s = "abaxabaxabb"
#     s = "abaxabaxabybaxabyb"
#     # s_even = "|".join(s)
#     # # s_even = "^" + "|".join(s) + "$"
#     s_len = len(s)
#     s_lst = [0] * s_len
#     center = radius = 0
#     for i in range(s_len):
#         s_lst[i] = max(s_lst[i], 1)
#
#
# long_palindr_substr_v3("abaxabaxabb")
# long_palindr_substr_v3("abaxabaxabybaxabyb")


# dev
