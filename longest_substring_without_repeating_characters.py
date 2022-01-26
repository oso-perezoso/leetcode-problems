# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0  # window start / end pos
        max_len = 0

        # we'll store { character: its last position in s }
        chars: Dict[str, int] = {}

        for end in range(len(s)):
            if s[end] in chars:  # duplicate character; reset start
                start = max(start, chars[s[end]] + 1)

            max_len = max(max_len, end - start + 1)
            chars[s[end]] = end

        return max_len
