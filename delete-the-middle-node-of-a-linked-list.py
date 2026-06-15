# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:   # 0 or 1 node — nothing to keep
            return None

        dummy = ListNode(0, head)       # sentinel: offsets slow by one step
        slow = dummy
        fast = head                     # fast starts at head, not dummy

        while fast and fast.next:
            slow = slow.next            # slow advances one step
            fast = fast.next.next       # fast advances two steps

        slow.next = slow.next.next      # skip (delete) the middle node
        return dummy.next
