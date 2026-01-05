"""Benchmark Longest Substring Without Repeating Characters."""

from __future__ import annotations

import random
import string
import typing

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_003_long_substr_no_repeat_chars

Args = tuple[str]


class BenchmarkLc003LongestSubstringWithoutRepeatingCharacters(BenchmarkBase[*Args, int]):
    """BenchmarkLc003LongestSubstringWithoutRepeatingCharacters."""

    funcs = (
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v1,
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v2,
        lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v3,
    )

    @classmethod
    def _data(cls, n: int) -> Args:
        return ("".join(random.choices(string.ascii_letters + string.digits, k=n)),)


BenchmarkLc003LongestSubstringWithoutRepeatingCharacters.register()


class BenchmarkLc003LongestSubstringWithoutRepeatingCharacters2(
    BenchmarkLc003LongestSubstringWithoutRepeatingCharacters,
):
    """BenchmarkLc003LongestSubstringWithoutRepeatingCharacters2."""

    @typing.override
    @classmethod
    def _data(cls, n: int) -> Args:
        return ("a" * n,)


# BenchmarkLc003LongestSubstringWithoutRepeatingCharacters2.register()
