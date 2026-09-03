class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1)%2==1 or sum(x&1 for x in nums1)==0
