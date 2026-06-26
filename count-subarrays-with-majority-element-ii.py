class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        valid_subarrays = 0
        current_sum = 0
        
        update(0 + offset, 1)
        
        for x in nums:
            if x == target:
                current_sum += 1
            else:
                current_sum -= 1
                
            valid_subarrays += query(current_sum + offset - 1)
            update(current_sum + offset, 1)
            
        return valid_subarrays
