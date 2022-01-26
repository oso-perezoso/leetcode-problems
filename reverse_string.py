# Reverse String
# https://leetcode.com/problems/reverse-string/


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i: int = 0
        j: int = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
