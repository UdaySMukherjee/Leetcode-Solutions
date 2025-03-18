class Solution {
    public int longestNiceSubarray(int[] nums) {
        int ans = 0;
        int mask = 0;
        for(int start = 0, end = 0; end < nums.length; ++end) {
            while((mask & nums[end]) != 0) {
                mask ^= nums[start++];
            }
            ans = Math.max(ans, end - start + 1);
            mask |= nums[end];
        }
        return ans;
    }
}
