# Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum: int = sum(nums[:k])
        max_sum: int = current_sum

        for i in range(1, len(nums) - k + 1):
            # update the sum:
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
