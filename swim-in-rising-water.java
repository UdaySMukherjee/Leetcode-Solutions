class Solution {

    private int n;
    private int m;

    private static final int[][] directions = {
        {-1, 0},
        {0, 1},
        {1, 0},
        {0, -1}
    };

    private boolean isInside(int i, int j) {
        return (i >= 0 && i < n && j >= 0 && j < m);
    }

    private void dfs(int[][] grid, boolean[][] visited, int mid, int row, int col) {
        visited[row][col] = true;

        for (int dir = 0; dir < 4; dir++) {
            int i = row + directions[dir][0];
            int j = col + directions[dir][1];

            if (isInside(i, j) && !visited[i][j] && grid[i][j] <= mid) {
                dfs(grid, visited, mid, i, j);
            }
        }
    }

    private boolean possible(int[][] grid, int mid) {
        // all grid values <= mid are allowed to traversed
        if (grid[0][0] > mid)
            return false;
        
        boolean[][] visited = new boolean[n][m];

        dfs(grid, visited, mid, 0, 0);

        return visited[n - 1][m - 1];
    }

    public int swimInWater(int[][] grid) {
        n = grid.length;
        m = grid[0].length;

        int low = 0;
        int high = n * n;

        int res = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (possible(grid, mid)) {
                res = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return res;
    }
}
