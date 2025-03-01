class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n, i=len(nums), 0
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums[i], nums[i+1]=nums[i]<<1, 0
                i+=1
            i+=1
        j=0
        for x  in nums:
            if x>0:
                nums[j]=x
                j+=1
        nums[j:]=[0]*(n-j)
        return nums
       
