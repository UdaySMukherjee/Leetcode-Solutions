class Solution {
    public int triangularSum(int[] nums) {
        while(nums.length > 1){
            int n = nums.length;
            int[] temp = new int[n-1];
            for(int i = 1; i < n; i++){
                temp[i-1] = (nums[i-1] + nums[i]) % 10;
            }
            nums = temp;
        }
        return nums[0];
    }
}
