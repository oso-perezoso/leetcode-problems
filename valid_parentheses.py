# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        parens: Dict[str, str] = {")": "(", "}": "{", "]": "["}

        stack: List[str] = []

        for c in s:
            if c in parens.values():
                stack.append(c)
            elif c in parens.keys():
                if len(stack) == 0 or stack.pop() != parens[c]:
                    return False

        return len(stack) == 0
