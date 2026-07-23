class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return n if (n:=len(nums))<3 else 1<<n.bit_length()
