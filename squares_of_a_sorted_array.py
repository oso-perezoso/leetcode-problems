# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result: List[int] = []

        i: int = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        # now i points to the first positive element

        j: int = i - 1  # j points to the last negative element

        while i < len(nums) and j >= 0:
            if nums[i] <= -nums[j]:
                result.append(nums[i] ** 2)
                i += 1
            else:
                result.append(nums[j] ** 2)
                j -= 1

        # If i < len(nums) and j < 0:
        while i < len(nums):
            result.append(nums[i] ** 2)
            i += 1

        # If j >= 0 and i >= len(nums):
        while j >= 0:
            result.append(nums[j] ** 2)
            j -= 1

        return result
