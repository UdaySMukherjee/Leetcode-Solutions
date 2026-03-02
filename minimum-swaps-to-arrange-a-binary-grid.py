class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n #first 1 position from right.
        for r in range(n):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    pos[r] = c
                    break
        #print(pos)
        ans = 0
        for r in range(n):
            k = -1
            for c in range(r, n):
                if pos[c] <= r: #can be switched with previous rows.
                    #ans += c - r #times of bubble up
                    k = c 
                    break

            if k != -1: #can be switched. do the bubble sort.
                for c in range(k, r, -1):
                    ans += 1
                    pos[c], pos[c - 1] = pos[c - 1], pos[c]
            else:
                return -1

        return ans
