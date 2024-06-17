class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m = int(math.sqrt(c))
        l, r = 0, m
        while l<=r:
            s = l*l + r*r 
            if s == c: return True 
            elif s < c:
                l += 1 
            else:
                r -= 1 
        return False
