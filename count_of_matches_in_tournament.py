# Count of Matches in Tournament
# https://leetcode.com/problems/count-of-matches-in-tournament/


class Solution:
    def numberOfMatches(self, n: int) -> int:
        result: int = 0

        while n != 1:
            result += n // 2
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1

        return result
