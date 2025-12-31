"""Benchmark Longest Substring Without Repeating Characters."""

from __future__ import annotations

import random
import string
import typing

import google_benchmark as benchmark

from leetcodes.lc_003_long_substr_no_repeat_chars import (
    long_substr_no_repeat_chars_v1,
    long_substr_no_repeat_chars_v2,
    long_substr_no_repeat_chars_v3,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


def setup_data_1(n: int) -> str:
    """Set up data."""
    return "a" * n


def setup_data_2(n: int) -> str:
    """Set up data."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
    """Decorate common params."""
    f = benchmark.option.range(64, 1 << 20)(f)
    # f = benchmark.option.range_multiplier(2)(f)
    return benchmark.option.complexity(benchmark.oAuto)(f)


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_1_v1(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_1(n)
    while state:
        long_substr_no_repeat_chars_v1(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_2_v1(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_2(n)
    while state:
        long_substr_no_repeat_chars_v1(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_1_v2(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_1(n)
    while state:
        long_substr_no_repeat_chars_v2(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_2_v2(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_2(n)
    while state:
        long_substr_no_repeat_chars_v2(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_1_v3(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_1(n)
    while state:
        long_substr_no_repeat_chars_v3(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_long_substr_no_repeat_chars_2_v3(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data_2(n)
    while state:
        long_substr_no_repeat_chars_v3(s)
    state.complexity_n = n
