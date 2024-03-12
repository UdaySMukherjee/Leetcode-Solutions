# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        LL = ListNode(0)
        LL.next = head
        Prefixsum = 0
        prefix_sum_map = {}
        current = LL

        while current is not None:
            Prefixsum += current.val
            if Prefixsum in prefix_sum_map:
                prev_node = prefix_sum_map[Prefixsum].next
                temp_sum = Prefixsum + prev_node.val
                while temp_sum != Prefixsum:
                    del prefix_sum_map[temp_sum]
                    prev_node = prev_node.next
                    temp_sum += prev_node.val
                prefix_sum_map[Prefixsum].next = current.next
            else:
                prefix_sum_map[Prefixsum] = current
            current = current.next 
        return LL.next
