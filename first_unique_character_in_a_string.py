# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Could use a dictionary, but we only use a-z letters:
        letter_count: List[int] = [0] * 26

        for c in s:
            letter_count[ord(c) - ord("a")] = letter_count[ord(c) - ord("a")] + 1

        for i, c in enumerate(s):
            if letter_count[ord(c) - ord("a")] == 1:
                return i

        return -1
