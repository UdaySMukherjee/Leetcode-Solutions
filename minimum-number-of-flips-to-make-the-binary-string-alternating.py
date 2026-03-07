class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        diff = 0
        
        for i in range(n):
            if int(s[i]) != (i & 1):
                diff += 1
                
        res = min(diff, n - diff)
        if res == 0 or (n & 1) == 0:
            return res
            
        for i in range(n):
            if int(s[i]) != (i & 1):
                diff -= 1
            else:
                diff += 1
                
            cur = min(diff, n - diff)
            if cur < res:
                res = cur
                if res == 0:
                    return 0
                    
        return res
