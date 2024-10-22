from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right.

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        # Step 1: Perform BFS to calculate the level sums
        level_sums = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)
        
        # Step 2: Sort the level sums in descending order
        level_sums.sort(reverse=True)
        
        # Step 3: Check if we have at least k levels
        if len(level_sums) < k:
            return -1
        
        # Step 4: Return the kth largest level sum
        return level_sums[k - 1]
