from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefixSum = [0] * (n + 1)
        
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        dq = deque()
        minLength = float('inf')
        
        for i in range(n + 1):
            while dq and prefixSum[i] - prefixSum[dq[0]] >= k:
                minLength = min(minLength, i - dq.popleft())
            
            while dq and prefixSum[i] <= prefixSum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return minLength if minLength != float('inf') else -1
