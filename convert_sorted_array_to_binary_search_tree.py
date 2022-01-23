# Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


from data_structures import TreeNode
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def _bst_rec(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None
            else:
                m: int = len(nums) // 2
                return TreeNode(nums[m], _bst_rec(nums[:m]), _bst_rec(nums[m + 1 :]))

        return _bst_rec(nums)
