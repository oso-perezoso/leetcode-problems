# Permutation in String
# https://leetcode.com/problems/permutation-in-string/


from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq: List[int] = [0] * 26
        s2_freq: List[int] = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

        for i in range(len(s2) - len(s1)):
            if s1_freq == s2_freq:
                return True

            s2_freq[ord(s2[i + len(s1)]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] -= 1

        return s1_freq == s2_freq
