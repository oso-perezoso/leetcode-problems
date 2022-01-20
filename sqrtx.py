# Sqrt(x)
# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        l: int = 0

        r: int = 1

        while r * r <= x:
            r = r * 2

        # Could set r = 46340, since
        # 46340^2 < 2^31 - 1 < 46341^2

        # Binary search for the rightmost element:
        while l < r:
            m: int = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1

        return r - 1
