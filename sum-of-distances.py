class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dist, cnt, prev = defaultdict(int), defaultdict(int), defaultdict(int)
        for i, num in enumerate(nums):
            dist[num] += i
            cnt[num] += 1
        arr = []
        for i, num in enumerate(nums):
            dist[num] -= (i - prev[num]) * cnt[num]
            arr.append(dist[num])
            cnt[num] -= 2
            prev[num] = i
        return arr
