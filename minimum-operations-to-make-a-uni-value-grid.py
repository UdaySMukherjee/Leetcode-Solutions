import numpy as np

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = np.array(grid).flatten()
    
        # Check feasibility: all elements must have same remainder modulo x
        if np.any((nums - nums[0]) % x != 0):
            return -1
    
        # The L1 minimizer is the median
        nums.sort()
        median = nums[len(nums) // 2]
    
        # Vectorized operation to find total steps
        return int(np.sum(np.abs(nums - median)) // x)        
