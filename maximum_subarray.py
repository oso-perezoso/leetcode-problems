# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# See https://en.wikipedia.org/wiki/Maximum_subarray_problem


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm, O(n)
        best_sum = -(2 ** 31)  # very small number, "-oo"
        current_sum = 0

        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)

        return best_sum
