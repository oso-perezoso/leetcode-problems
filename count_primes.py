# Count Primes
# https://leetcode.com/problems/count-primes/


from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        # Basic sieve
        is_prime: List[bool] = [True] * n
        is_prime[0] = is_prime[1] = False

        prime_count: int = 0

        for x, p in enumerate(is_prime):
            if p:
                prime_count += 1
                for y in range(x * x, n, x):
                    is_prime[y] = False

        return prime_count
