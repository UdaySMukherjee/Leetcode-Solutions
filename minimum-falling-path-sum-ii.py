class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DP = grid[0]

        for i in range(1, N):
            indx1 = DP.index(min(DP))
            indx2 = DP.index(min(DP[:indx1] + DP[indx1+1:]))
            for j in range(N):
                if j != indx1:
                    grid[i][j] += DP[indx1]
                else:
                    grid[i][j] += DP[indx2]
            DP = grid[i]

        return min(DP)
