class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0]) 
        
        # l1 = sum in the ROW direction, l2 = sum in COL direction 
        l1 = [0 for _ in range(ROWS)] 
        l2 = [0 for _ in range(COLS)]

        for r in range(ROWS): 
            for c in range(COLS): 
                l1[r] += grid[r][c] 
                l2[c] += grid[r][c] 
        
        # helper function, when given a summed list above, 
        # return True if there is a certain partition where left sum = right sum 
        def helper(l): 
            s = sum(l) 

            # check if a certain partition sum equal to total_sum / 2 
            a = 0 
            for x in l: 
                a += x 
                if a == s/2: 
                    return True 
            
            return False 

        return helper(l1) or helper(l2)
