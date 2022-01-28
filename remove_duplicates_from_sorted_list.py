# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


from data_structures import ListNode
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr: Optional[ListNode] = head

        while ptr is not None:
            while ptr.next is not None and ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            ptr = ptr.next

        return head
