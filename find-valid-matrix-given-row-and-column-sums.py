class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        result_matrix = [[0] * cols for _ in range(rows)]
        
        r, c = 0, 0
        while r < rows and c < cols:
            cell_value = min(rowSum[r], colSum[c])
            result_matrix[r][c] = cell_value
            
            rowSum[r] -= cell_value
            colSum[c] -= cell_value
            
            if rowSum[r] == 0:
                r += 1
            else:
                c += 1
        
        return result_matrix
