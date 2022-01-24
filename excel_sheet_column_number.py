# Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result: int = 0

        for c in columnTitle:
            result = 26 * result + ord(c) - ord("A") + 1

        return result
