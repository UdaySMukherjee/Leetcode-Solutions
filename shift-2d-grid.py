class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        if k == 0:
            return grid
            
        flat = [val for row in grid for val in row]
        shifted = flat[-k:] + flat[:-k]
        
        return [shifted[i * n : (i + 1) * n] for i in range(m)]
