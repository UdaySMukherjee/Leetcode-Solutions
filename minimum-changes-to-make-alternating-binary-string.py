import numpy as np

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        # Convert string to an array of 0s and 1s
        arr = np.array(list(s), dtype=int)
    
        # Create the two possible alternating patterns
        # Pattern 0: [0, 1, 0, 1, ...]
        # Pattern 1: [1, 0, 1, 0, ...]
        p0 = np.arange(n) % 2
        p1 = 1 - p0
    
        # Calculate mismatches
        diff0 = np.sum(arr != p0)
        diff1 = np.sum(arr != p1)
    
        return int(min(diff0, diff1))        
