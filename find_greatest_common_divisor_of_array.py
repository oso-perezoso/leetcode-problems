# Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/


from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def _gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            else:
                return _gcd(b, a % b)

        min_num: int = nums[0]
        max_num: int = nums[0]

        for x in nums:
            min_num = min(min_num, x)
            max_num = max(max_num, x)

        return _gcd(min_num, max_num)
