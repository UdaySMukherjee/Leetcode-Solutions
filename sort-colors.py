class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = [0, 0, 0]
        for i in nums:
            d[i] += 1
        
        for i in range(d[0]):
            nums[i] = 0

        for i in range(d[0], d[0] + d[1]):
            nums[i] = 1

        for i in range( d[0] + d[1], d[0] + d[1] + d[2]):
            nums[i] = 2
