"""BenchmarkLongest Palindromic Substring."""

from __future__ import annotations

import random
import string

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_005_long_palindr_substr

Args = tuple[str]


class BenchmarkLc005LongestPalindromicSubstring(BenchmarkBase[*Args, str]):
    """BenchmarkLc005LongestPalindromicSubstring."""

    funcs = (
        lc_005_long_palindr_substr.long_palindr_substr_v1,
        lc_005_long_palindr_substr.long_palindr_substr_v2,
    )

    @classmethod
    def _data(cls, n: int) -> Args:
        return ("".join(random.choices(string.ascii_letters + string.digits, k=n)),)


BenchmarkLc005LongestPalindromicSubstring.register()
