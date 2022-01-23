from typing import Optional


class ListNode:
    """Leetcode's singly-linked list node"""

    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class TreeNode:
    """Leetcode's binary tree node"""

    def __init__(
        self,
        val=0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
