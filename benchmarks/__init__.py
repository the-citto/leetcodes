"""Init."""

from __future__ import annotations

from benchmarks.benchmark_leetcodes import (
    BenchmarkLc001TwoSum,
    BenchmarkLc002AddTwoNumbers,
    BenchmarkLc003LongestSubstringWithoutRepeatingCharacters,
)

BenchmarkLc001TwoSum.register()
BenchmarkLc002AddTwoNumbers.register()
BenchmarkLc003LongestSubstringWithoutRepeatingCharacters.register()
