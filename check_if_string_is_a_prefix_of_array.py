# Check If String Is a Prefix of Array
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/submissions/


from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix_string: str = words[0]

        if s == prefix_string:
            return True

        for w in words[1:]:
            prefix_string = prefix_string + w
            if s == prefix_string:
                return True

        return False
