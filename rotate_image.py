# Rotate Image
# https://leetcode.com/problems/rotate-image/


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose and flip:

        # 1 2 3       1 4 7       7 4 1
        # 4 5 6  -->  2 5 8  -->  8 5 2
        # 7 8 9       3 6 9       9 6 3

        # 1. Transpose:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. Flip:
        for i in range(len(matrix)):
            j, k = 0, len(matrix[i]) - 1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
