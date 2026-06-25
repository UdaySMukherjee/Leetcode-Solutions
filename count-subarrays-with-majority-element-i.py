from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        op = 0

        for i in range(len(nums)):
            cnt = 0

            for j in range(i, len(nums)):
                if nums[j] == target:
                    cnt += 1
                else:
                    cnt -= 1

                if cnt > 0:
                    op += 1

        return op
