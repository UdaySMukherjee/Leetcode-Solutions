class Solution {
    public int numSubseq(int[] nums, int target) {
        final int MOD = 1_000_000_007;
        Arrays.sort(nums);
        int n = nums.length;
        int[] pow2 = new int[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            int want = target - nums[i];
            int idx = upperBound(nums, want);
            if (idx >= i) {
                res = (res + pow2[idx - i]) % MOD;
            }
        }

        return res;
    }

    private int upperBound(int[] A, int val) {
        int L = 0, H = A.length - 1, ans = -1;
        while (L <= H) {
            int M = L + (H - L) / 2;
            if (A[M] <= val) {
                ans = M;
                L = M + 1;
            } else {
                H = M - 1;
            }
        }
        return ans;
    }
}
