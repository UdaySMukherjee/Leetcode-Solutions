from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_len = 1
        
        if 1 in counts:
            ones_count = counts[1]
            if ones_count % 2 == 0:
                max_len = max(max_len, ones_count - 1)
            else:
                max_len = max(max_len, ones_count)
                
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while curr in counts and counts[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            if curr in counts:
                current_len += 1
            else:
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len
