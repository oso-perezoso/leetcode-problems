# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i: int = 0
        j: int = len(s) - 1

        while i < j:
            while i < j and not str.isalnum(s[i]):
                i += 1
            while i < j and not str.isalnum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
