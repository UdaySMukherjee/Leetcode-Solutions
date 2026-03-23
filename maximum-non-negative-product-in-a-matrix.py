class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mod = 1000000007
        dp = [[[9999999999, -1] for j in range(m)] for i in range(n)]
        dp[0][0] = [grid[0][0], grid[0][0]]
        for i in range(n):
            for j in range(m):
                g = grid[i][j]
                if i > 0:
                    p = dp[i-1][j][0] * g
                    q = dp[i-1][j][1] * g
                    dp[i][j][0] = min(dp[i][j][0], p, q)
                    dp[i][j][1] = max(dp[i][j][1], p, q)
                if j > 0:
                    p = dp[i][j-1][0] * g
                    q = dp[i][j-1][1] * g
                    dp[i][j][0] = min(dp[i][j][0], p, q)
                    dp[i][j][1] = max(dp[i][j][1], p, q)
        return max(dp[-1][-1]) % mod if max(dp[-1][-1]) >= 0 else -1
