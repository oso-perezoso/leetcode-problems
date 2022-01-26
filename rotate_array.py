# Rotate Array
# https://leetcode.com/problems/rotate-array/


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Example: [1,2,3,4,5,6,7], k = 3
        # Reverse: [7,6,5,4,3,2,1]
        # Reverse from 0 to 2: [5,6,7,4,3,2,1]
        # Reverse from 3 to 6: [5,6,7,1,2,3,4]

        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
