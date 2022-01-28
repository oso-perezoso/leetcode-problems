# Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
        next: Optional[Node] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# FIXME: couldn't figure out how to annotate types properly,
# so that the mypy typechecker doesn't complain...
class Solution:
    def connect(self, root):
        if root is None:
            return None

        level = [root]

        while True:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

            if level[0].left is None:
                return root

            next_level = []

            for node in level:
                next_level.append(node.left)
                next_level.append(node.right)

            level = next_level
