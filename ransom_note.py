# Ransom Note
# https://leetcode.com/problems/ransom-note/


from typing import Dict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_freq: Dict[str, int] = {}

        for c in magazine:
            letter_freq[c] = letter_freq.get(c, 0) + 1

        for c in ransomNote:
            if c not in letter_freq or letter_freq[c] == 0:
                return False
            else:
                letter_freq[c] = letter_freq[c] - 1

        return True
