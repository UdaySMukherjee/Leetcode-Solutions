class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        suffixSum = [0] * (n + 1)
        
        # Calculate suffix sums
        for i in range(n - 1, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + piles[i]
        
        # Fill DP table
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                for X in range(1, min(2 * M, n - i) + 1):
                    dp[i][M] = max(dp[i][M], suffixSum[i] - dp[i + X][max(M, X)])
        
        return dp[0][1]
