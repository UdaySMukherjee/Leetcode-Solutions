class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if (nums[i] in nums[:i]):
                nums.pop(i)
        return len(nums)
