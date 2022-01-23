# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        # The recurrence is
        #   F_1 = 1, F_2 = 2, F_n = F_{n-1} + F_{n-1}

        # Memoization:
        fib: list[int] = [1, 2]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])

        return fib[n - 1]
