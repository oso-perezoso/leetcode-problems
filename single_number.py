# Single Number
# https://leetcode.com/problems/single-number/


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for x in nums:
            xor_sum = xor_sum ^ x

        return xor_sum
