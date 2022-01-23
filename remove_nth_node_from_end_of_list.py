# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


from data_structures import ListNode
from typing import Optional


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if head is None:
            return None

        ptr1: Optional[ListNode] = head
        ptr2: Optional[ListNode] = head

        for _ in range(n + 1):  # advance ptr2 by (n+1) steps
            if ptr2 is None:  # reached the end; want to delete the head
                return head.next
            else:
                ptr2 = ptr2.next

        while ptr2 is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # ptr1 is now BEFORE the node to be deleted
        ptr1.next = ptr1.next.next
        return head
