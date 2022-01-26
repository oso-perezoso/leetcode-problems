# Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/


from data_structures import TreeNode
from typing import List, Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        level_nodes: List[TreeNode] = [root]
        depth: int = 1

        while len(level_nodes) != 0:
            next_level_nodes: List[TreeNode] = []

            for node in level_nodes:
                if node.left is None and node.right is None:  # leaf
                    return depth
                else:
                    if node.left is not None:
                        next_level_nodes.append(node.left)
                    if node.right is not None:
                        next_level_nodes.append(node.right)

            level_nodes = next_level_nodes
            depth += 1

        return -1  # never happens
