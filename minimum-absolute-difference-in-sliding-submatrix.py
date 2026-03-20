class Solution:
    def minAbsDiff(self, G: List[List[int]], k: int) -> List[List[int]]:
        return [[min((b - a for a, b in pairwise(sorted({ 
                G[rr][cc]
                for rr in range(r, r + k) 
                for cc in range(c, c + k) }))), default=0)
                for c in range(len(G[0]) - k + 1)]
                for r in range(len(G) - k + 1)]
