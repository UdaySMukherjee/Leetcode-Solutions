class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            data = abs(nums[i])
            index = data - 1
            if nums[index] < 0 :
                result.append(data)
            nums[index] *= -1
        return result       
