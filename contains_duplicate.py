# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elems: set = set()

        for x in nums:
            if x in elems:
                return True
            else:
                elems.add(x)

        return False
