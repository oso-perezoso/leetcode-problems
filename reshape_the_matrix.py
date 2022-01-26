# Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/


from typing import List


class Solution:
    def matrixReshape(
        self, mat: List[List[int]], r: int, c: int
    ) -> List[List[int]]:
        result: List[List[int]] = []
        for _ in range(r):
            result.append([0] * c)
        # Doing [[0] * c] * r would be wrong in Python

        r0: int = len(mat)

        if r0 == 0:
            return []

        c0: int = len(mat[0])

        if r0 * c0 != r * c:  # Illegal reshaping
            return mat

        i: int = 0  # element counter

        for row in mat:
            for x in row:
                result[i // c][i % c] = x
                i += 1

        return result
