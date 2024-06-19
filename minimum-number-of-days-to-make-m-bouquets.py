class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def condition(days) -> bool:
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                else:
                    bouquets += flowers // k
                    flowers = 0
            bouquets += flowers // k
            return bouquets >= m
            
        left = 1
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
