# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        index = list1
        for i in range(a-1):
            index = index.next

        temp = index.next
        for i in range(b-a+1):
            temp = temp.next

        index.next = list2 
        while list2.next is not None:
            list2 = list2.next

        list2.next = temp
        return list1
        
        
