class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        occurrence = 0
        count = 0
        D = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in D:
                if i - D.get(count) > occurrence:
                    occurrence = i - D.get(count)
            else:
                D[count] = i
            
            if count == 0:
                occurrence = i + 1
            
        return occurrence
