"""Main."""

# import google_benchmark as benchmark
#
#
# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []
#
#
# @benchmark.register
# # @benchmark.option.min_time(2.0)
# @benchmark.option.repetitions(3)
# # @benchmark.option.display_aggregates_only(True)
# @benchmark.option.range_multiplier(2)
# @benchmark.option.range(64, 1024)  # Keep range small while debugging
# @benchmark.option.complexity(benchmark.oAuto)
# def bm_two_sum_naive(state):
#     # Fetching the current range value
#     n = state.range(0)
#     # Setup data outside the timing loop
#     nums = list(range(n))
#     target = (n - 1) + (n - 2)
#     while state:
#         two_sum(nums, target)
#     # FIX: Assign to the property instead of calling it
#     state.complexity_n = n
#
#
# @benchmark.register
# # @benchmark.option.min_time(2.0)
# # @benchmark.option.repetitions(3)
# # @benchmark.option.display_aggregates_only(True)
# # @benchmark.option.range_multiplier(2)
# @benchmark.option.range(64, 1024)  # Keep range small while debugging
# @benchmark.option.complexity(benchmark.oAuto)
# def bm_two_sum(state):
#     # Fetching the current range value
#     n = state.range(0)
#     # Setup data outside the timing loop
#     nums = list(range(n))
#     target = (n - 1) + (n - 2)
#     while state:
#         two_sum(nums, target)
#     # FIX: Assign to the property instead of calling it
#     state.complexity_n = n
#
#
# if __name__ == "__main__":
#     benchmark.main()
