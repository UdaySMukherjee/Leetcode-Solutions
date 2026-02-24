# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node: TreeNode, n = 0)-> None:
            if not node: return

            n = 2 * n + node.val
            if not node.left and not node.right:
                self.ans+= n
                return
                
            dfs(node.left , n)
            dfs(node.right, n)
            return
            

        self.ans = 0
        dfs(root)
        return self.ans
