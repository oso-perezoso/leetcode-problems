# Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/


from array import array


class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Correct one-line pythonic solution:
        # return " ".join([w[::-1] for w in str.split(s, " ")])

        # 2. General in-place algorithm for mutable strings

        char_arr: array = array("u", s)  # mutable array of unicode chars

        def _reverse(s: array, i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        i: int = 0
        while i < len(char_arr):
            j: int = i

            # Make j point to the place after the word end:
            while j < len(char_arr) and char_arr[j] != " ":
                j += 1

            _reverse(char_arr, i, j - 1)

            i = j + 1

        return char_arr.tounicode()
