char** rotateTheBox(char** box, int boxSize, int* boxColSize, int* returnSize, int** returnColumnSizes) {
    int r = boxSize;       // Number of rows
    int c = *boxColSize;   // Number of columns

    *returnSize = c;       // Rotated matrix has `c` rows
    *returnColumnSizes = (int*)malloc(c * sizeof(int));
    char** rotate = (char**)malloc(c * sizeof(char*));

    // Initialize the rotated matrix
    for (int i = 0; i < c; i++) {
        rotate[i] = (char*)malloc(r * sizeof(char));
        memset(rotate[i], '.', r);  // Fill with empty spaces initially
        (*returnColumnSizes)[i] = r;
    }

    // Simulate gravity and populate rotated matrix
    for (int i = 0; i < r; i++) {
        int bottom = c - 1;  // Bottom pointer for gravity simulation
        for (int j = c - 1; j >= 0; j--) {
            if (box[i][j] == '#') {  // Stone
                rotate[bottom--][r - 1 - i] = '#';
            } else if (box[i][j] == '*') {  // Obstacle
                rotate[j][r - 1 - i] = '*';
                bottom = j - 1;  // Reset bottom pointer above the obstacle
            }
        }
    }

    return rotate;
}
