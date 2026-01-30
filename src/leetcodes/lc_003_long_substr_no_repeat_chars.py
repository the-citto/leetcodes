"""3. Longest Substring Without Repeating Characters.

URL:
    https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

from __future__ import annotations


def long_substr_no_repeat_chars_v1(s: str) -> int:
    """Longest Substring Without Repeating Characters."""
    max_len = 0
    for i in range(len(s)):
        substr = ""
        for ch in s[i:]:
            if ch in substr:
                break
            substr += ch
        max_len = max(max_len, len(substr))
    return max_len


def long_substr_no_repeat_chars_v2(s: str) -> int:
    """Longest Substring Without Repeating Characters."""
    max_len = 0
    for i in range(len(s)):
        substr: list[str] = []
        for ch in s[i:]:
            if ch in substr:
                break
            substr.append(ch)
        max_len = max(max_len, len(substr))
    return max_len


def long_substr_no_repeat_chars_v3(s: str) -> int:
    """Longest Substring Without Repeating Characters."""
    char_map: dict[str, int] = {}
    max_len = start = 0
    for i, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= start:
            start = char_map[ch] + 1
        else:
            max_len = max(max_len, i - start + 1)
        char_map[ch] = i
    return max_len
