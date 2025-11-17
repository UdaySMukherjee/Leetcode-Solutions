class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int prev = (int)-1e9;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (i - prev <= k) return false;
                prev = i;
            }
        }
        return true;
    }
}
