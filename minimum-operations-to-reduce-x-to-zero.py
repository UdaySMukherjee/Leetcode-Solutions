class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        N = len(nums)

        total = 0

        for num in nums:
            total += num

        target = total - x    

        left = current = 0

        best = float("-inf")

        for right in range(N):
            current += nums[right]
            while left <= right and current > target:
                current -= nums[left]
                left += 1
            if current == target:
                best = max(best, right-left+1)
        if best == float("-inf"):
            return -1
        return N - best      
