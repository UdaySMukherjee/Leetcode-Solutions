class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        min_moves = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                min_moves += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return min_moves
