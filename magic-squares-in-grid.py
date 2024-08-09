class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isMagicSquare(r, c):
            rows, cols, diag = [0, 0, 0], [0, 0, 0], [0, 0]
            s = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in s:
                        return False
                    s.add(val)
                    rows[i] += val
                    cols[j] += val
                    if i == j:
                        diag[0] += val
                    if i + j == 2:
                        diag[1] += val
            return (rows[0] == rows[1] == rows[2]) and (cols[0] == cols[1] == cols[2]) and (diag[0] == diag[1])
        
        return sum(isMagicSquare(r, c) for r in range(m - 2) for c in range(n - 2))
