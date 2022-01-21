# Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/solution/


from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a: int = 0

        for a in range(isqrt(c) + 1):
            b: int = c - a * a
            if b == isqrt(b) ** 2:
                return True

        return False
