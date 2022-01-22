# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Cf. https://en.wikipedia.org/wiki/Catalan_number
        def _paren_rec(n: int) -> List[str]:
            if n == 0:
                return [""]

            return [
                f"({x}){y}"
                for i in range(0, n)
                for x in _paren_rec(i)
                for y in _paren_rec(n - i - 1)
            ]

        return _paren_rec(n)
