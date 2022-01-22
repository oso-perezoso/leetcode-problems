# Permutations
# https://leetcode.com/problems/permutations/


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _perm_rec(nums: List[int]):
            if len(nums) == 0:
                return [[]]
            if len(nums) == 1:
                return [[nums[0]]]

            return [
                rest + [x]
                for i, x in enumerate(nums)
                for rest in _perm_rec(nums[:i] + nums[i + 1 :])
            ]

        return _perm_rec(nums)
