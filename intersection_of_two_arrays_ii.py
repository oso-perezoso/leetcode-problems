# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/


from typing import Dict, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def frequency_dict(arr: List[int]) -> Dict[int, int]:
            frequencies: Dict[int, int] = {}
            for x in arr:
                if x in frequencies:
                    frequencies[x] += 1
                else:
                    frequencies[x] = 1
            return frequencies

        freqs1: Dict[int, int] = frequency_dict(nums1)
        freqs2: Dict[int, int] = frequency_dict(nums2)

        result: List[int] = []

        for x in freqs1.keys():
            if x in freqs2:
                result += [x] * min(freqs1[x], freqs2[x])

        return result
