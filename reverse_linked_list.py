# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/


from data_structures import ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node: Optional[ListNode] = head
        prev_node: Optional[ListNode] = None
        next_node: Optional[ListNode] = None

        while curr_node is not None:
            next_node = curr_node.next  # remember next node
            curr_node.next = prev_node  # relink curr -> prev
            prev_node, curr_node = curr_node, next_node  # advance

        return prev_node

        # Example of how this works on [1,2,3,4]:
        #   Step 0: 1 -> 2 -> 3 -> 4 -> None
        #   Step 1: 1 -> None, 2 -> 3 -> 4 -> None
        #   Step 2: 2 -> 1 -> None, 3 -> 4 -> None
        #   Step 3: 3 -> 2 -> 1 -> None, 4 -> None
        #   Step 4: 4 -> 3 -> 2 -> 1 -> None
