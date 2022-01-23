# Missing Number
# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1 + 2 + ... + n = n*(n+1)/2
        n: int = len(nums)
        return n * (n + 1) // 2 - sum(nums)
