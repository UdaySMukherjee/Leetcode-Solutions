class Solution:
    def canReach(self, a: List[int], k: int) -> bool:
        return (f:=lambda i,d={-1}:0<=i<len(a) and i not in d and 
            (a[i]==0 or d.add(i) or f(i+a[i]) or f(i-a[i])))(k)
