# Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = [[1]]

        for i in range(1, numRows):
            result.append(
                [1]
                + [
                    result[i - 1][j] + result[i - 1][j + 1]
                    for j in range(i - 1)
                ]
                + [1]
            )

        return result
