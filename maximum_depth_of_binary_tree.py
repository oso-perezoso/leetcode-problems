# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from data_structures import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _depth_rec(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            else:
                return 1 + max(_depth_rec(root.left), _depth_rec(root.right))

        return _depth_rec(root)
