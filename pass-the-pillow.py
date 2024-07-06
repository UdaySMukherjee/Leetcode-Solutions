class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (x:=time% (N:=2*n-2)) < n:
            return 1+x
        else:
            return N+1-x
