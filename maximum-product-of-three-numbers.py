class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(prod(top := nlargest(3, nums)), top[0] * prod(nsmallest(2, nums)))
