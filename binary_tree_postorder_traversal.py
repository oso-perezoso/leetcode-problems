# Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/


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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive solution"""

        result: List[int] = []

        def _postorder_rec(root: Optional[TreeNode]) -> None:
            if root is not None:
                _postorder_rec(root.left)
                _postorder_rec(root.right)
                result.append(root.val)

        _postorder_rec(root)
        return result

    def postorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """Solution with stack"""

        result: List[int] = []
        stack: List[TreeNode] = []
        ptr: Optional[TreeNode] = root

        last_node_visited: Optional[TreeNode] = None

        while ptr is not None or len(stack) != 0:
            if ptr is not None:
                stack.append(ptr)
                ptr = ptr.left
            else:
                peek_ptr = stack[-1]
                # if right child exists and traversing ptr
                # from left child, then move right
                if (
                    peek_ptr.right is not None
                    and last_node_visited is not peek_ptr.right
                ):
                    ptr = peek_ptr.right
                else:
                    result.append(peek_ptr.val)
                    last_node_visited = stack.pop()

        return result
