class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = float('-inf')
        prefix = 1
        suffix = 1

        for j in range(0,len(nums)):
            prefix = prefix * nums[j]

            if(prefix>max):
                max = prefix

            if(prefix == 0):
                prefix = 1

        for k in range(len(nums)-1,0,-1):
            suffix = suffix * nums[k]

            if(suffix>max):
                max = suffix

            if(suffix == 0):
                suffix = 1

        return max
