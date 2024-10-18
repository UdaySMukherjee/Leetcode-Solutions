class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxBit = 0
        for num in nums:
            maxBit |= num


        res = [0]
        self.iteration(res, nums, 0, 0, maxBit)
        return res[0]
    
    def iteration(self, res, nums, i, bit_or, maxBit):
        if i >= len(nums):
            if bit_or == maxBit:
                res[0] += 1
            return


        self.iteration(res, nums, i+1, bit_or, maxBit)

        self.iteration(res, nums, i+1, bit_or | nums[i], maxBit)
