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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive solution"""

        result: List[int] = []

        def _inorder_rec(root: Optional[TreeNode]) -> None:
            if root is not None:
                _inorder_rec(root.left)
                result.append(root.val)
                _inorder_rec(root.right)

        _inorder_rec(root)
        return result

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """Solution with stack"""

        result: List[int] = []
        stack: List[TreeNode] = []
        ptr: Optional[TreeNode] = root

        while ptr is not None or len(stack) != 0:
            # Go to the leftmost node, putting nodes on the way on the stack:
            while ptr is not None:
                stack.append(ptr)
                ptr = ptr.left

            # Now we reached the end

            ptr = stack.pop()
            result.append(ptr.val)

            # We'll go to the right now:
            ptr = ptr.right

        return result
