# Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # See Legendre's formula for v_p (n!)
        # https://en.wikipedia.org/wiki/Legendre%27s_formula
        def _legendre(n: int, p: int) -> int:
            v: int = 0
            i: int = 1

            while p ** i <= n:
                v += n // p ** i
                i += 1

            return v

        return min(_legendre(n, 2), _legendre(n, 5))
