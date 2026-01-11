"""BenchmarkLongest Palindromic Substring."""

from __future__ import annotations

import random
import string
import typing

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_005_long_palindr_substr

Args = tuple[str]


class BenchmarkLc005LongestPalindromicSubstring(BenchmarkBase[*Args, str]):
    """BenchmarkLc005LongestPalindromicSubstring."""

    @classmethod
    def _data(cls, n: int) -> Args:
        return ("".join(random.choices(string.ascii_letters + string.digits, k=n)),)

    @typing.override
    @classmethod
    def _bm_name(cls, func_name: str) -> str:
        _ = func_name
        return cls.__name__


# BenchmarkLc005LongestPalindromicSubstring.register()


class BenchmarkLc005LongestPalindromicSubstringNaive(BenchmarkLc005LongestPalindromicSubstring):
    """BenchmarkLc005LongestPalindromicSubstringNaive."""

    funcs = (lc_005_long_palindr_substr.long_palindr_substr_v1,)
    bm_range = (1 << 4, 1 << 11)


class BenchmarkLc005LongestPalindromicSubstringManacher(BenchmarkLc005LongestPalindromicSubstring):
    """BenchmarkLc005LongestPalindromicSubstringManacher."""

    funcs = (lc_005_long_palindr_substr.long_palindr_substr_v2,)


class BenchmarkLc005LongestPalindromicSubstringUkkonen(BenchmarkLc005LongestPalindromicSubstring):
    """BenchmarkLc005LongestPalindromicSubstringUkkonen."""

    funcs = (lc_005_long_palindr_substr.long_palindr_substr_v3,)


BenchmarkLc005LongestPalindromicSubstringNaive.register()
BenchmarkLc005LongestPalindromicSubstringManacher.register()
BenchmarkLc005LongestPalindromicSubstringUkkonen.register()
