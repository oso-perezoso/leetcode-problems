# Pow(x,n)
# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        def pow_rec(x: float, n: int) -> float:
            if n == 0:
                return 1

            y: float = pow_rec(x, n // 2)

            if n % 2 == 1:
                return x * y * y
            else:
                return y * y

        return pow_rec(x, n)
