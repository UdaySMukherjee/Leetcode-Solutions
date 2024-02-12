class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i, val in enumerate(nums):
            rem = target - val
            if rem in sol:
                return [sol[rem], i]
            sol[val] = i
        return []
                
                
            
        