# Find the Difference
# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter_sum: int = 0

        for c in t:
            letter_sum = letter_sum + ord(c)

        for c in s:
            letter_sum = letter_sum - ord(c)

        return chr(letter_sum)
