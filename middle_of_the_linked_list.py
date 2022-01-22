# Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/


from data_structures import ListNode
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Clever solution: have a pointer that moves two positions ahead
        ptr: Optional[ListNode] = head

        while ptr is not None:
            ptr = ptr.next

            if ptr is not None:
                ptr = ptr.next
            else:
                break

            if head is not None:
                head = head.next

        return head
