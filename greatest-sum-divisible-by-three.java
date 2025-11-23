class Solution {
    public int maxSumDivThree(int[] nums) {
        int[]dp=new int[3];
        dp[0]=0;
        dp[1]=Integer.MIN_VALUE;
        dp[2]=dp[1];
        for(int val:nums){
            int[]curr=dp.clone();
            for(int i=0;i<dp.length;i++){
                curr[(i+val)%3]=Math.max(curr[(i+val)%3],dp[i]+val);
            }
            dp=curr;
        }
        return dp[0];
    }
}
