# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set: set = set(jewels)

        count: int = 0

        for s in stones:
            if s in jewel_set:
                count += 1

        return count
