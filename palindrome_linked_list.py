# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/


from data_structures import ListNode
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # See middle_of_the_linked_list.py
        def _mid_node(head: Optional[ListNode]) -> Optional[ListNode]:
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

        # See reverse_linked_list.py
        def _reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            curr_node: Optional[ListNode] = head
            prev_node: Optional[ListNode] = None
            next_node: Optional[ListNode] = None

            while curr_node is not None:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node, curr_node = curr_node, next_node

            return prev_node

        def _list_eq(
            head1: Optional[ListNode], head2: Optional[ListNode]
        ) -> bool:
            while head1 is not None and head2 is not None:
                if head1.val != head2.val:
                    return False
                head1, head2 = head1.next, head2.next

            return True

        mid: Optional[ListNode] = _mid_node(head)
        rev: Optional[ListNode] = _reverse(mid)
        return _list_eq(head, rev)
