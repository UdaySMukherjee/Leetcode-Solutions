class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] capacity = new double[query_row+2][query_row+2];
        capacity[0][0] = poured;

        for(int i = 0;i <= query_row;i++){
            for(int j = 0;j <= i;j++){
                if(capacity[i][j] > 1) {
                    double extra = capacity[i][j] - 1;
                    capacity[i][j] = 1;
                    capacity[i + 1][j] += extra / 2;
                    capacity[i + 1][j + 1] += extra / 2;
                }
            }
        }

        return capacity[query_row][query_glass];
    }
}
