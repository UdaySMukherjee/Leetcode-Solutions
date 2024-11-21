int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize, int** walls, int wallsSize, int* wallsColSize) {
    char** grid = (char**)malloc(m * sizeof(char*));
    for (int i = 0; i < m; i++) {
        grid[i] = (char*)malloc(n * sizeof(char));
        for (int j = 0; j < n; j++) {
            grid[i][j] = '.';
        }
    }
    for (int i = 0; i < guardsSize; i++) {
        int row = guards[i][0];
        int col = guards[i][1];
        grid[row][col] = 'G';
    }
    for (int i = 0; i < wallsSize; i++) {
        int row = walls[i][0];
        int col = walls[i][1];
        grid[row][col] = 'W';
    }
    int** guarded = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        guarded[i] = (int*)calloc(n, sizeof(int));
    }
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    for (int i = 0; i < guardsSize; i++) {
        int row = guards[i][0];
        int col = guards[i][1];
        for (int d = 0; d < 4; d++) {
            int dr = directions[d][0];
            int dc = directions[d][1];
            int r = row + dr, c = col + dc;
            while (r >= 0 && r < m && c >= 0 && c < n) {
                if (grid[r][c] == 'W' || grid[r][c] == 'G') break;
                guarded[r][c] = 1;
                r += dr;
                c += dc;
            }
        }
    }
    int count = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == '.' && !guarded[i][j]) {
                count++;
            }
        }
    }
    return count;
}
