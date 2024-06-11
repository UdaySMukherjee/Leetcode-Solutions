
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        t = [0] * 1001
        ans = []

        for x in arr1:
            t[x] += 1

        for y in arr2:
            while t[y] != 0:
                ans.append(y)
                t[y] -= 1

        for i in range(len(t)):
            while t[i] != 0:
                ans.append(i)
                t[i] -= 1

        return ans

