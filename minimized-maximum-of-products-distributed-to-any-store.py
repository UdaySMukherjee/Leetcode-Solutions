import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)
        res = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            stores_needed = sum(math.ceil(quantity / mid) for quantity in quantities)
            
            if stores_needed <= n:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
