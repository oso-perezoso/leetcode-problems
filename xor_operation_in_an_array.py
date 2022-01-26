# XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s: int = 0

        for i in range(n):
            s ^= start + 2 * i

        return s
