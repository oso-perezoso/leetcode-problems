# N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/


from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        trib: List[int] = [0, 1, 1]
        while len(trib) <= n:
            trib.append(trib[-1] + trib[-2] + trib[-3])

        return trib[n]
