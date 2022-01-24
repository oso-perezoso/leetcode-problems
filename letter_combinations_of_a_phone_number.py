# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def _comb_rec(digits: str) -> List[str]:
            if len(digits) == 0:
                return [""]
            else:
                return [
                    c + suf
                    for c in mapping[digits[0]]
                    for suf in _comb_rec(digits[1:])
                ]

        if digits == "":
            return []
        else:
            return _comb_rec(digits)
