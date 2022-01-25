# Merge Intervals
# https://leetcode.com/problems/merge-intervals/


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # It would be better to work with List[Tuple[int,int]]
        intervals.sort(key=lambda x: x[0])

        result: List[List[int]] = []
        result.append(intervals[0])

        for i in intervals[1:]:
            if i[0] <= result[-1][1]:
                result[-1][1] = max(i[1], result[-1][1])
            else:
                result.append(i)

        return result
