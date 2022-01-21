# Two Sum
# https://leetcode.com/problems/two-sum/


from typing import Dict, List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        # Dictionary to store { number: position }
        diff_dict: Dict[int, int] = {}

        for i, x in enumerate(nums):
            j: Optional[int] = diff_dict.get(target - x)
            if j is not None:
                return [j, i]

            diff_dict[x] = i

        return None
