# Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/


import re
from typing import Optional, Tuple


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def _parse_num(num: str) -> Tuple[int, int]:
            m: Optional[re.Match] = re.search("(-?\d+)\+(-?\d+)", num)
            if m:
                return (int(m.groups()[0]), int(m.groups()[1]))
            else:
                return (0, 0)

        def _mul_num(
            num1: Tuple[int, int], num2: Tuple[int, int]
        ) -> Tuple[int, int]:
            x1, y1 = num1
            x2, y2 = num2
            return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)

        def _num_to_str(num: Tuple[int, int]) -> str:
            return f"{num[0]}+{num[1]}i"

        return _num_to_str(_mul_num(_parse_num(num1), _parse_num(num2)))
