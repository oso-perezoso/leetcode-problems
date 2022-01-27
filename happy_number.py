# Happy Number
# https://leetcode.com/problems/happy-number/


from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        def _digit_squares(n: int) -> int:
            square_sum: int = 0
            while n != 0:
                square_sum = square_sum + (n % 10) ** 2
                n = n // 10
            return square_sum

        numbers: Set[int] = {n}

        while n != 1:
            n = _digit_squares(n)
            if n in numbers:  # loop detected
                return False
            else:
                numbers.add(n)

        return True
