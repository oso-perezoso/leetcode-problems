# Sort Colors
# https://leetcode.com/problems/sort-colors/


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Counting sort (quick, two-pass)"""
        count: List[int] = [0, 0, 0]

        for x in nums:
            count[x] += 1

        i: int = 0

        for j in (0, 1, 2):
            for _ in range(count[j]):
                nums[i] = j
                i += 1

    def sortColorsOnePass(self, nums: List[int]) -> None:
        """One-pass solution (slower in Python)"""
        i: int = 0
        j: int = 0
        k: int = len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:  # nums[i] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
