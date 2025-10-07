class Solution:
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n
        dry_days = []
        last_rain = {}

        for i in range(n):
            if rains[i] == 0:
                insort(dry_days, i)
                ans[i] = 1
            else:
                lake = rains[i]
                if lake in last_rain:
                    last_day = last_rain[lake]
                    idx = bisect_right(dry_days, last_day)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake
                    dry_days.pop(idx)
                last_rain[lake] = i
        return ans
        
