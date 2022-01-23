# Power of Two
# https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n & 1 != 0:  # n != 0 (mod 2)
                return False
            else:
                n = n >> 1  # divide by 2

        return True
