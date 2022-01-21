# Move Zeroes
# https://leetcode.com/problems/move-zeroes/submissions/


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i: int = 0
        j: int = 0

        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j = j + 1

            if j < len(nums):
                nums[i] = nums[j]
                i, j = i + 1, j + 1

        while i < len(nums):
            nums[i] = 0
            i = i + 1
