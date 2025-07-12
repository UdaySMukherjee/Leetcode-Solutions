class Solution {
    private Map<Integer,int[]> memo = new HashMap<>();
    public int[] earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        memo.clear();
        return dp(firstPlayer, n - secondPlayer + 1, n);
    }
    private int[] dp(int l, int r, int k) {
        if (l == r) return new int[]{1, 1};
        if (l > r) return dp(r, l, k);
        int key = (l << 10) | (r << 5) | k;
        if (memo.containsKey(key)) return memo.get(key);
        int half_k  = k / 2;
        int half_k1 = (k + 1) / 2;
        int min_s = l + r - half_k;
        int max_s = half_k1;
        int a = Integer.MAX_VALUE, b = Integer.MIN_VALUE;
        for (int i = 1; i <= l; ++i) {
            int low1  = l - i + 1;
            int high1 = r - i;
            int low2  = min_s - i;
            int high2 = max_s - i;
            int j_low  = low1  > low2  ? low1  : low2;
            int j_high = high1 < high2 ? high1 : high2;
            if (j_low > j_high) continue;
            for (int j = j_low; j <= j_high; ++j) {
                int[] pr = dp(i, j, half_k1);
                a = pr[0] + 1 < a ? pr[0] + 1 : a;
                b = pr[1] + 1 > b ? pr[1] + 1 : b;
            }
        }
        int[] ans = new int[]{a, b};
        memo.put(key, ans);
        return ans;
    }
}
