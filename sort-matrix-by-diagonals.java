class Solution {
    // Main method - the boss that coordinates everything! 👔
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;  // Get the size of our grid
        
        // Process ↘️ descending diagonals (starting from first column)
        for (int i = 0; i < n; i++) 
            sortDiagonal(grid, i, 0, false);  // false = big to small
        
        // Process ↗️ ascending diagonals (starting from first row, skip [0,0])
        for (int j = 1; j < n; j++) 
            sortDiagonal(grid, 0, j, true);   // true = small to big
        
        return grid;  // Return the sorted matrix
    }
    
    // Helper method - the worker that sorts one diagonal at a time! 🛠️
    private void sortDiagonal(int[][] grid, int row, int col, boolean increasing) {
        int n = grid.length;
        List<Integer> diagonal = new ArrayList<>();  // Temporary storage

        // Step 1: Collect all elements along the diagonal 📦
        int i = row, j = col;
        while (i < n && j < n) {
            diagonal.add(grid[i][j]);  // Grab the number
            i++; j++;  // Move diagonally down-right
        }
        
        // Step 2: Sort in the required direction 🔄
        if (increasing) {
            Collections.sort(diagonal);  // Small → Big ↗️
        } else {
            Collections.sort(diagonal, Collections.reverseOrder());  // Big → Small ↘️
        }
        
        // Step 3: Put sorted numbers back where they came from 📥
        i = row; j = col;  // Reset to starting position
        int idx = 0;  // Index for our sorted list
        while (i < n && j < n) {
            grid[i][j] = diagonal.get(idx++);  // Place sorted number
            i++; j++;  // Move to next diagonal position
        }
    }
}
