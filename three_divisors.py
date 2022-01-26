# Three Divisors
# https://leetcode.com/problems/three-divisors/


from math import isqrt


class Solution:
    def isThree(self, n: int) -> bool:
        # n has three divisors iff n = p^2 for prime p

        def _is_prime(n: int) -> bool:
            if n < 2:
                return False

            for x in range(2, int(isqrt(n)) + 1):
                if n % x == 0:
                    return False

            return True

        sq: int = isqrt(n)
        return n == sq ** 2 and _is_prime(sq)
