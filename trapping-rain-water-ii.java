class Cell {
    int height;
    int row;
    int col;
    Cell(int height, int row, int col) {
        this.height = height;
        this.row = row;
        this.col = col;
    }
}
class Solution {
    public boolean check(int x, int y, int n, int m) {
        return x>=0 && y>=0 && x<n && y<m;
    }
    public int trapRainWater(int[][] heightMap) {
        int n = heightMap.length;
        int m = heightMap[0].length;
        int ans = 0;
        PriorityQueue<Cell> pq = new PriorityQueue<>(new Comparator<>(){
            @Override
            public int compare(Cell a, Cell b) {
                return Integer.compare(a.height, b.height);
            }
        });
        boolean vis[][] = new boolean[n][m];
        for(int i=0;i<n;i++) {
            pq.add(new Cell(heightMap[i][0], i, 0));
            pq.add(new Cell(heightMap[i][m-1], i, m-1));
            vis[i][0] = vis[i][m-1] = true;
        }
        for(int i=0;i<m;i++) {
            pq.add(new Cell(heightMap[0][i], 0, i));
            pq.add(new Cell(heightMap[n-1][i], n-1, i));
            vis[0][i] = vis[n-1][i] = true;
        }
        int[][] dir = {{0,1}, {0,-1}, {-1,0}, {1,0}};
        while(!pq.isEmpty()) {
            Cell cell = pq.remove();
            for(int i=0;i<4;i++) {
                int x = cell.row + dir[i][0];
                int y = cell.col + dir[i][1];
                if(check(x,y,n,m) && vis[x][y] == false) {
                    if(heightMap[x][y] < cell.height) {
                        ans += (cell.height - heightMap[x][y]);
                        pq.add(new Cell(cell.height, x, y));
                    } else {
                        pq.add(new Cell(heightMap[x][y], x, y));
                    }
                    vis[x][y] = true;
                }
            }
        }
        return ans;
    }
}
