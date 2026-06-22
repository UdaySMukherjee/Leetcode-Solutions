class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min((f:=Counter(text))['a'], f['b'], f['l']>>1, f['o']>>1, f['n'] )
