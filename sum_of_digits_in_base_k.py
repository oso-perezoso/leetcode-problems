# Sum of Digits in Base K
# https://leetcode.com/problems/sum-of-digits-in-base-k/


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        else:
            digit_sum: int = 0
            while n != 0:
                digit_sum += n % k
                n = n // k
            return digit_sum
