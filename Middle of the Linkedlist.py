# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        LL = ListNode(0)
        LL.next = head

        current1 = LL
        current2 = LL

        while current1.next is not None and current1.next.next is not None:
            current2 = current2.next
            current1 = current1.next.next
        
        return current2.next
        
        
