# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/


from data_structures import TreeNode
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _is_mirror(
            root1: Optional[TreeNode], root2: Optional[TreeNode]
        ) -> bool:
            if root1 is None and root2 is None:
                return True
            elif root1 is not None and root2 is not None:
                return (
                    root1.val == root2.val
                    and _is_mirror(root1.left, root2.right)
                    and _is_mirror(root1.right, root2.left)
                )
            else:
                return False

        return root is None or _is_mirror(root.left, root.right)
