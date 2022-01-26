# Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/


from typing import Dict, List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freqs: Dict[int, int] = {}

        for x in nums:
            freqs[x] = freqs.get(x, 0) + 1

        return sum((fr * (fr - 1) // 2 for fr in freqs.values()))
