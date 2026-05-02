# so basically, we only want numbers that contain 2s, 5, 6s ,and 9s
# 10 ** 4 = 10000
# it can be 4 digits
# it has to have at least 1 2, 5, 6, or 9, and it cannot have a 3, 4, or 7
# [2, 5, 6, 9, 25, 26, 29, 52, 56, 59]
nums = []
for n in range(1, 10**4+1):
    s = str(n)
    if ("2" in s or "5" in s or "6" in s or "9" in s) and ("3" not in s and "4" not in s and "7" not in s):
        nums.append(n)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        return bisect.bisect(nums, n) 
