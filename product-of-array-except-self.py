class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list = [0 for i in range(len(nums))]
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]
        # print(nums)

        prefix[0] = nums[0]
        for j in range(1,len(nums)):
            prefix[j] = prefix[j-1] * nums[j]
        # print(prefix)

        suffix[-1] = nums[-1]
        for k in range(len(nums)-2,-1,-1):
            suffix[k] = suffix[k+1] * nums[k]
        # print(suffix)
        suffix.append(1)

        list[0] = suffix[1]
        for i in range(1,len(nums)):
            list[i] = prefix[i-1] * suffix[i+1]
        return list
        
