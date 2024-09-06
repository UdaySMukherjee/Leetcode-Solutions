class Solution:
    def modifiedList(self, excludeValues: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        exclude_set = set(excludeValues)
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val in exclude_set:
                curr.next = curr.next.next  
            else:
                curr = curr.next  
        
        return dummy.next

def list_to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    inputs = map(loads, sys.stdin)
    results = []

    for excludeValues in inputs:
        head_list = next(inputs)
        head = list_to_linked_list(head_list)
        
        filtered_head = Solution().modifiedList(excludeValues, head)
        results.append(linked_list_to_list(filtered_head))

    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)

if __name__ == "__main__":
    main()
    sys.exit(0)

#Stolen From kartikdevsharmaa
#https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/submissions/1373611245/
