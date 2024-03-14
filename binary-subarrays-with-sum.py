class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0 : 1}
        cumulative_sum = 0
        subset = 0

        for i in nums:
            cumulative_sum += i
            if cumulative_sum-goal in freq:
                subset += freq[cumulative_sum-goal]
            freq[cumulative_sum] = freq.get(cumulative_sum,0) + 1

        return subset
