# Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count: int = 0

        while n != 0:
            bit_count = bit_count + (n & 1)
            n = n >> 1

        return bit_count
