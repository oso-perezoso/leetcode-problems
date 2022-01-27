# Flood Fill
# https://leetcode.com/problems/flood-fill/


from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        rows: int = len(image)
        cols: int = len(image[0])

        oldColor: int = image[sr][sc]

        if oldColor == newColor:
            return image

        def _fill_rec(sr: int, sc: int) -> None:
            if image[sr][sc] == oldColor:
                image[sr][sc] = newColor
                if sr > 0:
                    _fill_rec(sr - 1, sc)
                if sr < rows - 1:
                    _fill_rec(sr + 1, sc)
                if sc > 0:
                    _fill_rec(sr, sc - 1)
                if sc < cols - 1:
                    _fill_rec(sr, sc + 1)

        _fill_rec(sr, sc)
        return image
