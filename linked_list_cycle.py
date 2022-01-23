# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/


from data_structures import ListNode
from typing import Set, Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited: Set[ListNode] = set()

        while head is not None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False
