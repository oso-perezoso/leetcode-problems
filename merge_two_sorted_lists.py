# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


from data_structures import ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head: ListNode = ListNode()
        ptr: ListNode = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ptr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ptr.next = ListNode(list2.val)
                list2 = list2.next
            ptr = ptr.next

        while list1 is not None:
            ptr.next = ListNode(list1.val)
            list1 = list1.next
            ptr = ptr.next

        while list2 is not None:
            ptr.next = ListNode(list2.val)
            list2 = list2.next
            ptr = ptr.next

        return head.next
