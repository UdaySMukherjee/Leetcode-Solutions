class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        mx, mn = [-inf, -inf], [-inf]

        for num in nums:
            heappushpop(mx,  num)
            heappushpop(mn, -num)

        return sum((*mx, *mn))
