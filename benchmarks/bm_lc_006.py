"""Benchmark Zigzag Conversion."""

from __future__ import annotations

import random
import string

from benchmarks.benchmark_base import BenchmarkBase
from leetcodes import lc_006_zigzag_conversion

Args = tuple[str, int]


class BenchmarkLc006ZigzagConversion(BenchmarkBase[*Args, str]):
    """BenchmarkLc006ZigzagConversion."""

    funcs = (lc_006_zigzag_conversion.zigzag_conversion_v1, lc_006_zigzag_conversion.zigzag_conversion_v2)

    @classmethod
    def _data(cls, n: int) -> Args:
        return ("".join(random.choices(string.ascii_letters + string.digits, k=n)), 5)


BenchmarkLc006ZigzagConversion.register()
