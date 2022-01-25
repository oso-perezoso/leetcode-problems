# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r: int = len(matrix)  # guaranteed >= 1
        c: int = len(matrix[0])

        result: List[int] = []

        i, j = 0, 0
        i_min, i_max = 0, r - 1
        j_min, j_max = 0, c - 1
        i_dir, j_dir = 0, 1

        for _ in range(r * c):
            result.append(matrix[i][j])
            i, j = i + i_dir, j + j_dir

            if j > j_max:
                i_min = i_min + 1
                i, j = i + 1, j - 1
                i_dir, j_dir = 1, 0
            elif i > i_max:
                j_max = j_max - 1
                i, j = i - 1, j - 1
                i_dir, j_dir = 0, -1
            elif j < j_min:
                i_max = i_max - 1
                i, j = i - 1, j + 1
                i_dir, j_dir = -1, 0
            elif i < i_min:
                j_min = j_min + 1
                i, j = i + 1, j + 1
                i_dir, j_dir = 0, 1

        return result
