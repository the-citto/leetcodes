"""Main."""

import importlib

import google_benchmark as benchmark

importlib.import_module("bm_lc_001_two_sums")
importlib.import_module("bm_lc_002_add_two_numbers")


if __name__ == "__main__":
    benchmark.main()


# @benchmark.option.complexity(benchmark.oAuto)
# @benchmark.option.display_aggregates_only(True)
# @benchmark.option.min_time(2.0)
# @benchmark.option.range(64, 1024)
# @benchmark.option.range_multiplier(2)
# @benchmark.option.repetitions(3)
