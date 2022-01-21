# Subsets
# https://leetcode.com/problems/subsets/


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            [nums[i] for i in range(len(nums)) if mask & (1 << i) != 0]
            for mask in range(2 ** len(nums))
        ]
