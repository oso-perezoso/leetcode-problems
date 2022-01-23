# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


from typing import List, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> Optional[List[int]]:
        i: int = 0
        j: int = len(numbers) - 1

        while i < j:
            s: int = numbers[i] + numbers[j]

            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i = i + 1
            else:
                j = j - 1

        return None
