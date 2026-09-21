class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = []
        heapq.heappush(heap, -a)
        heapq.heappush(heap, -b)
        heapq.heappush(heap, -c)
        res = 0
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            res += 1
            first += 1
            second += 1
            if first < 0:
                heapq.heappush(heap, first)
            if second < 0:
                heapq.heappush(heap, second)
        return res
