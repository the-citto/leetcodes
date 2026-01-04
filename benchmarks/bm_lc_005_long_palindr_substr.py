"""BenchmarkLongest Palindromic Substring."""

from __future__ import annotations

import random
import string
import typing

import google_benchmark as benchmark

from leetcodes.lc_005_long_palindr_substr import (
    long_palindr_substr_v1,
    long_palindr_substr_v2,
)

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


def setup_data(n: int) -> str:
    """Set up data."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def common_params[T](f: Callable[..., T] | OptionMaker.Options) -> Callable[..., T] | OptionMaker.Options:
    """Decorate common params."""
    f = benchmark.option.range(1 << 4, 1 << 11)(f)
    return benchmark.option.complexity(benchmark.oAuto)(f)


@benchmark.register
@common_params
def bm_lc_005_v1(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data(n)
    while state:
        long_palindr_substr_v1(s)
    state.complexity_n = n


@benchmark.register
@common_params
def bm_lc_005_v2(state: benchmark.State) -> None:
    """Benchmark Two Sum."""
    n = state.range(0)
    s = setup_data(n)
    while state:
        long_palindr_substr_v2(s)
    state.complexity_n = n
