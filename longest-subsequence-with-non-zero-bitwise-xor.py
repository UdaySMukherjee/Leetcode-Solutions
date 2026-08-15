class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        return 0 if all(x==0 for x in nums) else len(nums)-(reduce(xor, nums, 0)==0)
