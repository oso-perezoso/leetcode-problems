# Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/


from typing import List, Set


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def _digits(n: int) -> Set[int]:
            if n == 0:
                return {0}
            else:
                digits = set()
                while n != 0:
                    digits.add(n % 10)
                    n //= 10
                return digits

        def _self_divisible(n: int) -> bool:
            digits: Set[int] = _digits(n)
            return 0 not in digits and all([n % d == 0 for d in digits])

        return [x for x in range(left, right + 1) if _self_divisible(x)]
