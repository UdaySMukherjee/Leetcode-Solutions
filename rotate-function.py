class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        Sum=sum(nums)
        ans=F=sum(i*x for i, x in enumerate(nums))
        for k in range(1, n):
            F+=Sum-n*nums[n-k]
            ans=max(ans, F)
        return ans
        
