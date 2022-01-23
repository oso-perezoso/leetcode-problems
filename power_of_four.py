# Power of Four
# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n & 11 != 0:  # n != 0 (mod 4)
                return False
            else:
                n = n >> 2  # divide by 4

        return True
