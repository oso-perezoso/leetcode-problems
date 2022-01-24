# Majority Element
# https://leetcode.com/problems/majority-element/


from typing import Dict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Basic solution with a frequency dictionary (hash map)
        freqs: Dict[int, int] = {}
        target_freq: int = len(nums) // 2

        for x in nums:
            fr: int = freqs.get(x, 0)

            if fr >= target_freq:
                return x

            freqs[x] = fr + 1

        return 0
