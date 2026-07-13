class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = 0
        max_gain = 0
        gains = {} 
        
        for x in nums:
            if x == k:
                total_k += 1
            else:
                gains[x] = max(gains.get(x, 0), total_k) + 1
                max_gain = max(max_gain, gains[x] - total_k)
                
        return total_k + max_gain
