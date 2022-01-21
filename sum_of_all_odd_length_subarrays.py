# Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        array_sum: int = 0

        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                array_sum = array_sum + sum(arr[i : j + 1])

        return array_sum
