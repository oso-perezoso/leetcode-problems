# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/


from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        # We'll work with a list of characters
        # to illustrate the general in-place approach:
        chars: List[str] = list(s)

        def _is_vowel(c: str) -> bool:
            return c in "AEIOUaeiou"

        i: int = 0
        j: int = len(chars) - 1

        while i < j:
            while i < j and not _is_vowel(chars[i]):
                i += 1
            while i < j and not _is_vowel(chars[j]):
                j -= 1

            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)
