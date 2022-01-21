# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/


from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1: Set[int] = set(nums1)
        set2: Set[int] = set(nums2)

        return [x for x in set1 if (x in set2)]
