class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        times = []
        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            times.append(hours * 60 + minutes)
        
        times.sort()
        
        min_diff = float('inf')

        for i in range(len(times) - 1):
            min_diff = min(min_diff, times[i + 1] - times[i])
        
        min_diff = min(min_diff, 1440 + times[0] - times[-1])
        
        return min_diff
