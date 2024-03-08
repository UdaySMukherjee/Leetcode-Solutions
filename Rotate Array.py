class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = nums.copy()
        for i in range(len(nums)):
            j=(i+k)%len(nums)
            nums[j] = nums1[i]
            
