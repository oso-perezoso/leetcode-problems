# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l: int = 0

        r: int = 1

        while r * r <= num:
            r = r * 2

        # Could set r = 46340, since
        # 46340^2 < 2^31 - 1 < 46341^2

        # Usual binary search:
        while l <= r:
            m: int = (l + r) // 2
            sqr: int = m * m

            if sqr < num:
                l = m + 1
            elif sqr > num:
                r = m - 1
            else:
                return True

        return False
