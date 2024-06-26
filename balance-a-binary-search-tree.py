# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform inorder traversal
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Helper function to build a balanced BST from sorted values
        def build_balanced_bst(sorted_values):
            if not sorted_values:
                return None
            mid = len(sorted_values) // 2
            node = TreeNode(sorted_values[mid])
            node.left = build_balanced_bst(sorted_values[:mid])
            node.right = build_balanced_bst(sorted_values[mid + 1:])
            return node
        
        # Get sorted values from the BST
        sorted_values = inorder_traversal(root)
        # Build and return a balanced BST
        return build_balanced_bst(sorted_values)
