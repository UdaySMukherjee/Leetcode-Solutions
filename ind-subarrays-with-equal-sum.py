class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        i=0
        freq={}
        if len(nums)<3:
            return False
        else:
            for i in range(len(nums)-1):
                s=nums[i]+nums[i+1]
                freq[s]=freq.get(s,0)+1
                if freq.get(s,0)>1:
                    return True
                else:
                    freq[s]=freq.get(s,0)+1        
        return False
