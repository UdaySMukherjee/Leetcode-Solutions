class Solution {
    public int countSubarrays(int[] nums) {
        int count = 0;
        for(int i=1;i<nums.length-1;i++){
            if(0.5*nums[i]==nums[i-1]+nums[i+1]){
                count++;
            }
        }
        return count;
    }
}
