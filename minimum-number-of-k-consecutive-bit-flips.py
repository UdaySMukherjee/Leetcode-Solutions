class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        acc, toggle = [0] * len(nums), 0

        for idx, num in enumerate(nums):
            
            if idx >= k: toggle ^= acc[idx -k]      # <-- toggle change-digit if we leave a flip interval

            if toggle != num: continue              # <-- num is not a change digit

            if k > len(nums)-idx: return -1         # <-- num is a change digit but we can't flip anymore

            toggle ^= 1                             # <-- num is a change-digit we can flip, so toggle
            acc[idx] = 1                            #     the change-digit and record it in acc.

        return sum(acc)                             # <-- return the number of flips
