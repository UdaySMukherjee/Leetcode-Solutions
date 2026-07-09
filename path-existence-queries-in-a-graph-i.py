class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0]*n

        curr_group = 0

        for i in range(1 ,n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_group += 1
            group[i] = curr_group
        
        res = []
        for u, v in queries:
            res.append(group[u] == group[v])
        return res
        
