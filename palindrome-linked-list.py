# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half_reversed = reverse(slow)
        first_half = head

        while second_half_reversed:
            if first_half.val != second_half_reversed.val:
                return False
            first_half = first_half.next
            second_half_reversed = second_half_reversed.next

        return True
