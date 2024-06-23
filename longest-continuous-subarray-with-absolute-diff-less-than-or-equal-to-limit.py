class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = collections.deque()
        min_q = collections.deque()
        l = 0
        max_len = 0
        
        for r in range(len(nums)):
            # Maintain max_q as a non-increasing deque
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            # Maintain min_q as a non-decreasing deque
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            
            max_q.append(nums[r])
            min_q.append(nums[r])
            
            # Check the condition max_q[0] - min_q[0] > limit
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
            
            # Calculate the length of the current valid subarray
            max_len = max(max_len, r - l + 1)
        
        return max_len
