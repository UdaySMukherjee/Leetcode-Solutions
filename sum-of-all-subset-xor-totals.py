class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            # Base case: when all elements have been considered
            if index == len(nums):
                return current_xor
            # Include nums[index] in the subset
            include = dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index] from the subset
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)
