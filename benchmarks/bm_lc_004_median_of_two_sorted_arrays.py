"""Benchmark Median of Two Sorted Arrays."""

from __future__ import annotations

import random
import typing

import google_benchmark as benchmark

from leetcodes.lc_004_median_of_two_sorted_arrays import (
    median_of_two_sorted_arrays_v1,
    median_of_two_sorted_arrays_v2,
    median_of_two_sorted_arrays_v3,
    median_of_two_sorted_arrays_v4,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


def setup_data(n: int) -> tuple[list[int], list[int]]:
    """Set up data."""
    full_list = sorted(random.sample(range(n * 10), n))
    return full_list[::2], full_list[1::2]


def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
    """Decorate common params."""
    f = benchmark.option.range(8, 1 << 20)(f)
    return benchmark.option.complexity(benchmark.oAuto)(f)


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_v1(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums1, nums2 = setup_data(n)
    while state:
        median_of_two_sorted_arrays_v1(nums1, nums2)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_v2(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums1, nums2 = setup_data(n)
    while state:
        median_of_two_sorted_arrays_v2(nums1, nums2)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_v3(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums1, nums2 = setup_data(n)
    while state:
        median_of_two_sorted_arrays_v3(nums1, nums2)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_v4(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    nums1, nums2 = setup_data(n)
    while state:
        median_of_two_sorted_arrays_v4(nums1, nums2)
    state.complexity_n = n
