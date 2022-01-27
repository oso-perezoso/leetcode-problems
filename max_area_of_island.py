# Max Area of Island
# https://leetcode.com/problems/max-area-of-island/


from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        # We'll keep a set of land coordinates (i,j)
        # and remove them after visiting

        land: Set[Tuple[int, int]] = {
            (i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1
        }

        def _area_rec(i: int, j: int) -> int:
            if (i, j) in land:
                land.remove((i, j))  # mark the spot as visited
                return (
                    1
                    + _area_rec(i - 1, j)
                    + _area_rec(i + 1, j)
                    + _area_rec(i, j - 1)
                    + _area_rec(i, j + 1)
                )

            else:
                return 0

        max_area = 0

        while land:
            for i, j in land:
                # Because there is only set.pop()...
                max_area = max(max_area, _area_rec(i, j))
                break

        return max_area
