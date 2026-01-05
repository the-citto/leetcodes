"""Benchamrk leetcodes."""

from __future__ import annotations

import abc
import typing

import google_benchmark as benchmark

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from google_benchmark import (
        __OptionMaker as OptionMaker,  # pyright: ignore[reportPrivateUsage]
    )


class BenchmarkBase[*P, T](abc.ABC):
    """BenchmarkBase."""

    funcs: tuple[Callable[[*P], T], ...]
    best_only = True
    common_range = (1 << 4, 1 << 11)

    @classmethod
    @abc.abstractmethod
    def _data(cls, n: int) -> tuple[*P]:
        """Return benchmark data."""

    @classmethod
    def _params(
        cls,
        f: Callable[[benchmark.State], None] | OptionMaker.Options,
    ) -> Callable[[benchmark.State], None] | OptionMaker.Options:
        f = benchmark.option.range(*cls.common_range)(f)
        return benchmark.option.complexity(benchmark.oAuto)(f)

    @classmethod
    def _bm_factory(cls, target_func: Callable[[*P], T]) -> None:
        def _make_bm(
            f: Callable[[*P], T],
        ) -> Callable[[benchmark.State], None]:
            def _bm_wrapper(state: benchmark.State) -> None:
                n = state.range(0)
                _data = cls._data(n)
                while state:
                    f(*_data)
                state.complexity_n = n

            func_v = f.__name__.split("_")[-1]  # ty: ignore [unresolved-attribute]
            _bm_wrapper.__name__ = f"{cls.__name__}_{func_v}"
            return _bm_wrapper

        bm_func: Callable[[benchmark.State], None] | OptionMaker.Options = _make_bm(target_func)
        bm_func = cls._params(bm_func)
        benchmark.register(bm_func)

    @classmethod
    def register(cls) -> None:
        """Register functions."""
        if cls.best_only:
            cls._bm_factory(cls.funcs[-1])
        else:
            for target_func in cls.funcs:
                cls._bm_factory(target_func)


# class BenchmarkLc002AddTwoNumbers(BenchmarkBase[*tuple[list[int], list[int]], list[int]]):
#     """BenchmarkLc002AddTwoNumbers."""
#
#     funcs = (
#         lc_002_add_two_numbers.add_two_numbers_v1,
#         lc_002_add_two_numbers.add_two_numbers_v2,
#         lc_002_add_two_numbers.add_two_numbers_v3,
#         lc_002_add_two_numbers.add_two_numbers_v4,
#     )
#
#     @classmethod
#     def _data(cls, n: int) -> tuple[list[int], list[int]]:
#         l1 = [1] * n
#         l2 = [1] * n
#         return l1, l2


# class BenchmarkLc003LongestSubstringWithoutRepeatingCharacters(BenchmarkBase[*tuple[str], int]):
#     """BenchmarkLc003LongestSubstringWithoutRepeatingCharacters."""
#
#     funcs = (
#         lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v1,
#         lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v2,
#         lc_003_long_substr_no_repeat_chars.long_substr_no_repeat_chars_v3,
#     )
#
#     @classmethod
#     def _data(cls, n: int) -> tuple[str]:
#         return ("".join(random.choices(string.ascii_letters + string.digits, k=n)),)
#         # return "a" * n


# class BenchmarkLc004MedianOfTwoSortedArrays(BenchmarkBase[*tuple[list[int], list[int]], float]):
#     """BenchmarkLc004MedianOfTwoSortedArrays."""
#
#     funcs = (
#         lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v1,
#         lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v2,
#         lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v3,
#         lc_004_median_of_two_sorted_arrays.median_of_two_sorted_arrays_v4,
#     )
#
#     @classmethod
#     def _data(cls, n: int) -> tuple[list[int], list[int]]:
#         full_list = sorted(random.sample(range(n * 10), n))
#         return full_list[::2], full_list[1::2]
#
#
# class BenchmarkLc005LongestPalindromicSubstring(BenchmarkBase[*tuple[str], str]):
#     """BenchmarkLc005LongestPalindromicSubstring."""
#
#     funcs = (lc_005_long_palindr_substr.long_palindr_substr_v1,)
#
#     @classmethod
#     def _data(cls, n: int) -> tuple[str]:
#         return ("".join(random.choices(string.ascii_letters + string.digits, k=n)),)
