class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # Number of Paths With Max Score
        n=len(board)
        dp=[[[float('-inf'),0] for _ in range(n)] for _ in range(n)]
        dp[-1][-1][0]=0
        dp[-1][-1][1]=1
        # print(int(board[0][1]))
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]!='X' and board[i][j]!='S':
                    max_val=max((dp[i][j+1][0] if j+1<n else float('-inf')),(dp[i+1][j][0] if i+1<n else float('-inf')))
                    max_val=max(max_val,dp[i+1][j+1][0] if i+1<n and j+1<n else float('-inf'))
                    dp[i][j][0]=max_val+(int(board[i][j]) if board[i][j]!='E' else 0)
                    if j+1<n and dp[i][j+1][0]==max_val :
                        dp[i][j][1]+=dp[i][j+1][1]
                    if i+1<n and dp[i+1][j][0]==max_val :
                        dp[i][j][1]+=dp[i+1][j][1]
                    if i+1<n and j+1<n and dp[i+1][j+1][0]==max_val:
                        dp[i][j][1]+=dp[i+1][j+1][1]
                dp[i][j][1]%=(10**9+7)
        return dp[0][0] if dp[0][0][0]!=float('-inf') else [0,dp[0][0][1]]
