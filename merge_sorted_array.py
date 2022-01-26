# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/


from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        k: int = len(nums1) - 1  # pointer to the part that will be filled
        i: int = m - 1  # pointer to nums1
        j: int = n - 1  # pointer to nums2

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
