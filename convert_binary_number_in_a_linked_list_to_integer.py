# Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


from data_structures import ListNode
from typing import Optional


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result: int = 0

        while head is not None:
            result = (result << 1) | head.val
            head = head.next

        return result
