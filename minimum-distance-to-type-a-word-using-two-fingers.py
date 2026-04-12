class Solution:
    def minimumDistance(self, word: str) -> int:
        # Helper function to calculate Manhattan distance between two characters
        def dist(c1, c2):
            if c1 is None or c2 is None:
                return 0
            # Get coordinates on keyboard (X-Y plane)
            # A is at (0,0), B at (0,1), ... Z at (4,1)
            x1, y1 = divmod(ord(c1) - ord('A'), 6)
            x2, y2 = divmod(ord(c2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        # dp[i][j] = min distance to type word[0:i] with one finger at word[i-1] and other at j
        # j can be any previous character index or -1 (not placed yet)
        dp = {}
        
        def solve(pos, f1, f2):
            # pos: current position in word
            # f1, f2: positions of finger 1 and finger 2 (-1 if not placed)
            if pos == n:
                return 0
            
            if (pos, f1, f2) in dp:
                return dp[(pos, f1, f2)]
            
            curr = word[pos]
            
            # Option 1: Move finger 1 to current character
            cost1 = float('inf')
            if f1 == -1:
                cost1 = solve(pos + 1, pos, f2)
            else:
                cost1 = dist(word[f1], curr) + solve(pos + 1, pos, f2)
            
            # Option 2: Move finger 2 to current character
            cost2 = float('inf')
            if f2 == -1:
                cost2 = solve(pos + 1, f1, pos)
            else:
                cost2 = dist(word[f2], curr) + solve(pos + 1, f1, pos)
            
            dp[(pos, f1, f2)] = min(cost1, cost2)
            return dp[(pos, f1, f2)]
        
        return solve(0, -1, -1)
