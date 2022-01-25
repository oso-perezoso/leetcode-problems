# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/


from typing import List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _block_check(
            board: List[List[str]], i0: int, i1: int, j0: int, j1: int
        ) -> bool:
            nums: Set[str] = set()

            for i in range(i0, i1 + 1):
                for j in range(j0, j1 + 1):
                    if board[i][j] != ".":
                        if board[i][j] in nums:
                            return False
                        else:
                            nums.add(board[i][j])

            return True

        # Row check
        if not all((_block_check(board, i, i, 0, 8) for i in range(9))):
            return False

        # Column check
        if not all((_block_check(board, 0, 8, j, j) for j in range(9))):
            return False

        # 3 x 3 block check
        if not all(
            (
                _block_check(board, i, i + 2, j, j + 2)
                for i in range(0, 9, 3)
                for j in range(0, 9, 3)
            )
        ):
            return False

        return True
