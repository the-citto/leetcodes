"""Main."""

import importlib

import google_benchmark as benchmark

importlib.import_module("bm_lc_001_two_sums")
importlib.import_module("bm_lc_002_add_two_numbers")


if __name__ == "__main__":
    benchmark.main()
