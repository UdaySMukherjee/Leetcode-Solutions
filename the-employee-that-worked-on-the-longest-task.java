class Solution {
    public int hardestWorker(int n, int[][] logs) {
        int diff = logs[0][1];
        int finalId = logs[0][0];

        for(int i = 1; i < logs.length; i++){
            int currDiff = logs[i][1] - logs[i - 1][1];

            if(currDiff > diff){
                diff = currDiff;
                finalId = logs[i][0];
            }

            if(currDiff == diff){
                finalId = Math.min(finalId, logs[i][0]);
            }
        }

        return finalId;
    }
}
