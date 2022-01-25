# Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r: int = len(matrix)  # number of rows

        if r == 0:
            return False

        c: int = len(matrix[0])  # number of columns

        lo: int = 0
        hi: int = r * c - 1

        while lo <= hi:
            m: int = (lo + hi) // 2

            i: int = m // c
            j: int = m % c

            if matrix[i][j] < target:
                lo = m + 1
            elif matrix[i][j] > target:
                hi = m - 1
            else:
                return True

        return False
