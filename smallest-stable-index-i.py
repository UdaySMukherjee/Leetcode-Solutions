class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        xMax=-1
        for i, s in enumerate(list(accumulate(nums[::-1], min))[::-1]):
            xMax=max(xMax, nums[i])
            if xMax-s<=k: return i
        return -1
