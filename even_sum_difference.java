class Solution {
    public int countPartitions(int[] nums) {
        int sum = 0;
        for(int i = 0; i < nums.length; i++) sum += nums[i];  
        if(sum % 2 == 0) return nums.length - 1;
        return 0;
    }
}