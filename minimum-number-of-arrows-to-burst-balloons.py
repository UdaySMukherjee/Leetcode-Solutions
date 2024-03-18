class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()

        prev = points[0]
        count = 1

        for i in range(1,n):
            currentStart = points[i][0]
            currentEnd = points[i][1]

            prevStart = prev[0]
            prevEnd = prev[1]

            if currentStart > prevEnd: #no overlap
                count += 1
                prev = points[i]
            else: #overlap
                prev[0] = max(prevStart, currentStart)
                prev[1] = min(prevEnd, currentEnd)

        return count
