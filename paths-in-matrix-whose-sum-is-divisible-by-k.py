class Solution(object):
    MOD = 10**9 + 7

    def numberOfPaths(self, grid, k):
        m, n = len(grid), len(grid[0])

        # dp[i][j][sum_mod]
        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def dfs(i, j, sum_mod):
            sum_mod = (sum_mod + grid[i][j]) % k

            # Base case
            if i == m - 1 and j == n - 1:
                return 1 if sum_mod == 0 else 0

            if dp[i][j][sum_mod] != -1:
                return dp[i][j][sum_mod]

            down = right = 0
            if i + 1 < m:
                down = dfs(i + 1, j, sum_mod)
            if j + 1 < n:
                right = dfs(i, j + 1, sum_mod)

            dp[i][j][sum_mod] = (down + right) % self.MOD
            return dp[i][j][sum_mod]

        return dfs(0, 0, 0)
