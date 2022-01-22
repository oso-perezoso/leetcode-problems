# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from data_structures import TreeNode
from typing import List, Optional


# Reminder:
#
# Depth-first search <---> stack structure
#
# Traversal types:
#   inorder   :  left - root  - right
#   preorder  :  root - left  - right
#   postorder :  left - right - root


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive solution"""

        result: List[int] = []

        def _preorder_rec(root: Optional[TreeNode]) -> None:
            if root is not None:
                result.append(root.val)
                _preorder_rec(root.left)
                _preorder_rec(root.right)

        _preorder_rec(root)
        return result

    def preorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """Solution with stack"""

        result: List[int] = []
        stack: List[TreeNode] = []
        ptr: Optional[TreeNode] = root

        if ptr is None:
            return []
        else:
            stack.append(ptr)

        while len(stack) != 0:
            ptr = stack.pop()
            result.append(ptr.val)

            # right child is pushed first so that left is processed first
            if ptr.right is not None:
                stack.append(ptr.right)
            if ptr.left is not None:
                stack.append(ptr.left)

        return result
