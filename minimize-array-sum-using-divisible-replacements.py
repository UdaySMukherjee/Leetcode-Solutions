class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        total_sum=0
        n=len(nums)
        maximum=0
        for value in nums:
            maximum=max(value,maximum)
        flag=[False]*(maximum + 1)
        for value in nums:
            flag[value]=True
        div=[0]*(maximum+1)
        for i in range(1,maximum+1):
            if not flag[i]:
                continue
            for j in range(i,maximum+1,i):
                if div[j]==0:
                    div[j]=i
        for value in nums:
            total_sum+=div[value]
        return total_sum    
