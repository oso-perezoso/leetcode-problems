# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head: ListNode = ListNode()
        result_ptr: ListNode = head

        c: int = 0  # carry

        while l1 is not None or l2 is not None or c != 0:
            x: int = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next

            y: int = 0
            if l2 is not None:
                y = l2.val
                l2 = l2.next

            s: int = x + y + c

            if s > 9:
                s, c = s % 10, (s - s % 10) // 10
            else:
                c = 0

            result_ptr.next = ListNode(s)
            result_ptr = result_ptr.next

        return head.next
