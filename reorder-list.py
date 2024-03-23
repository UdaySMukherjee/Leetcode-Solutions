# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next
        slow.next = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        p1 = head
        p2 = prev
        while p2 is not None:
            next_p1 = p1.next
            next_p2 = p2.next
            p1.next = p2
            p2.next = next_p1
            p1 = next_p1
            p2 = next_p2
