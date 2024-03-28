class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        frequency = {}
        left = 0
        for right in range(len(nums)):
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1
            if frequency[nums[right]] > k:
                while nums[left] != nums[right]:
                    frequency[nums[left]] -= 1
                    left += 1
                frequency[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
 
