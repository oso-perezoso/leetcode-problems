# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i: int = 1
        j: int = 1

        while j < len(nums):
            while j < len(nums) and nums[j] == nums[j - 1]:
                j = j + 1

            if j < len(nums):
                nums[i] = nums[j]
                i, j = i + 1, j + 1

        return i
