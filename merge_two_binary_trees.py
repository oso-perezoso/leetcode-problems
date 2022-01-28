# Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/


from data_structures import TreeNode
from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def _merge_rec(
            root1: Optional[TreeNode], root2: Optional[TreeNode]
        ) -> Optional[TreeNode]:
            if root1 is not None and root2 is not None:
                return TreeNode(
                    root1.val + root2.val,
                    _merge_rec(root1.left, root2.left),
                    _merge_rec(root1.right, root2.right),
                )
            elif root1 is not None and root2 is None:
                return root1
            elif root1 is None and root2 is not None:
                return root2
            else:
                return None

        return _merge_rec(root1, root2)
