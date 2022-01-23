# Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/


from data_structures import ListNode


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        if node.next is not None:  # always the case for this problem
            node.val = node.next.val
            node.next = node.next.next
            # (since we don't know the previous node)
