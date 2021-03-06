# Implement strStr()
# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # This is the naive algorithm, for more sophisticated approaches,
        # see https://en.wikipedia.org/wiki/String-searching_algorithm

        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1
