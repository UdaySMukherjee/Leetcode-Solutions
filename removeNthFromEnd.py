# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        LL = ListNode(0)
        LL.next = head
        current1 = LL
        current2 = LL
        for i in range(0,n):
            current1 = current1.next

        while current1.next is not None:
            current1 = current1.next
            current2 = current2.next
        
        current2.next = current2.next.next

        return LL.next
