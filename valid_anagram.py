# Valid Anagram
# https://leetcode.com/problems/valid-anagram/


from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq: List[int] = [0] * 26

        if len(s) != len(t):
            return False

        for c in s:
            letter_freq[ord(c) - ord("a")] = letter_freq[ord(c) - ord("a")] + 1
        for c in t:
            letter_freq[ord(c) - ord("a")] = letter_freq[ord(c) - ord("a")] - 1

        for fr in letter_freq:
            if fr != 0:
                return False

        return True
