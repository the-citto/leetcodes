"""3. Longest Substring Without Repeating Characters.

Given a string `s`, find the length of the **longest substring** without duplicate characters.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


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
