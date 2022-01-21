# First Bad Version
# https://leetcode.com/problems/first-bad-version/


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    raise NotImplementedError


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Leftmost binary search:
        l: int = 1
        r: int = n

        while l < r:
            m: int = (l + r) // 2

            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l
