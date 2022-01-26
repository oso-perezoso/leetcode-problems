# Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/


from data_structures import ListNode
from typing import Optional


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        def _list_len(head: Optional[ListNode]) -> int:
            l: int = 0

            while head is not None:
                head = head.next
                l += 1

            return l

        lenA: int = _list_len(headA)
        lenB: int = _list_len(headB)

        ptrA: Optional[ListNode] = headA
        ptrB: Optional[ListNode] = headB

        if lenA < lenB:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next

        if lenB < lenA:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next

        while ptrA is not None and ptrB is not None:
            if ptrA is ptrB:
                return ptrA

            ptrA, ptrB = ptrA.next, ptrB.next

        return None
