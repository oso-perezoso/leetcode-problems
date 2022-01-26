# Plus One
# https://leetcode.com/problems/plus-one/


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result: List[int] = []
        c: int = 1  # carry

        for d in reversed(digits):
            s: int = d + c

            if s > 9:
                s, c = s % 10, s // 10
            else:
                c = 0

            result.append(s)

        if c != 0:
            result.append(c)

        return list(reversed(result))
