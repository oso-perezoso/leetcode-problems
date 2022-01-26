# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/


from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: Set[int] = set(nums)

        max_len: int = 0

        for x in num_set:
            if x - 1 not in num_set:
                # A consecutive sequence starts from x;
                # calculate its length
                y: int = x
                new_len: int = 0

                while y in num_set:
                    y += 1
                    new_len += 1

                max_len = max(max_len, new_len)

        return max_len
