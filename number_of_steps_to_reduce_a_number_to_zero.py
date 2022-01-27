# Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        result: int = 0

        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num = num >> 1
            result += 1

        return result
