class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long sum = 0;
        int neg = 0, min = Integer.MAX_VALUE;
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix.length; j++) {
                int val = Math.abs(matrix[i][j]);
                if(matrix[i][j] < 0) neg++; 
                if(val < min) min = val;
                sum += val;
            }
        }
        return (neg & 1) == 0 ? sum : sum - 2 * min;
    }
}
