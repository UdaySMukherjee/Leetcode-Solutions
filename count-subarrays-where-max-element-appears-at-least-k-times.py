class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M=max(nums)
        cnt=0
        ans=0
        l=0
        for r in range(len(nums)):
            if nums[r]==M:
                cnt+=1
            while cnt>=k:
                if nums[l]==M:
                    cnt-=1
                l+=1
            ans+=l
        return ans
