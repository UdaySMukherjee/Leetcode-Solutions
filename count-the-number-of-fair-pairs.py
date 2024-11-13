class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort() 
        def countp(target):
            count = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
            return count
        totalup = countp(upper)
        totallo = countp(lower - 1)
        return totalup - totallo

