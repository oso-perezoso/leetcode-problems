# Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/


from data_structures import ListNode
from typing import Optional


class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        """Non-recursive solution"""
        while head is not None and head.val == val:
            head = head.next

        ptr: Optional[ListNode] = head

        while ptr is not None:
            ptr2: Optional[ListNode] = ptr.next

            while ptr2 is not None and ptr2.val == val:
                ptr2 = ptr2.next

            ptr.next = ptr2
            ptr = ptr.next

        return head

    def removeElementsRec(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        """Recursive solution"""

        def _remove_elem_rec(
            head: Optional[ListNode], val: int
        ) -> Optional[ListNode]:
            if head is None:
                return None
            elif head.val == val:
                return _remove_elem_rec(head.next, val)
            else:
                head.next = _remove_elem_rec(head.next, val)
                return head

        return _remove_elem_rec(head, val)
