from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        lastOcc = {}
        lastOcc[self.reverse(nums[0])] = 0

        INF = 10**18
        res = INF

        for j in range(1, len(nums)):
            if nums[j] in lastOcc:
                res = min(res, j - lastOcc[nums[j]])
            lastOcc[self.reverse(nums[j])] = j

        return -1 if res == INF else res
