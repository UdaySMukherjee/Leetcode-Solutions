class Solution {
    public int findFinalValue(int[] nums, int original) {
        int ans = original;
        int[] hash = new int[1001];
        for(int i = 0; i < nums.length; i++) hash[nums[i]]++;
        while(ans <= 1000 && hash[ans] != 0) ans *= 2;
        return ans;
    }
}
