from heapq import heappop, heappush
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Priority queue to store tuples in the form (total_time, (original_time, iteration))
        pq = []

        # Initialize the priority queue with worker times
        for time in workerTimes:
            heappush(pq, (time, time, 1)) # (current time, original time, iteration count)

        ans = 0

        # Process each height increment of the mountain
        for _ in range(mountainHeight):
            currentTime, originalTime, iteration = heappop(pq)
            ans = currentTime

            # Push the next time for this worker back into the priority queue
            heappush(pq, (currentTime + originalTime * (iteration + 1), originalTime, iteration + 1))

        return ans
