class Solution {
    static final int MOD = 1_000_000_007;
    static int MAX = 10010;
    long[][] comb = new long[MAX][20];

    public int idealArrays(int n, int maxValue) {
        // Precompute combinations C(n, k)
        for (int i = 0; i < MAX; ++i) {
            comb[i][0] = 1;
        }

        for (int i = 1; i < MAX; ++i) {
            for (int j = 1; j < 20; ++j) {
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD;
            }
        }

        // cnt[k][v] = number of sequences of length k ending with value v
        int[][] cnt = new int[20][maxValue + 1];
        for (int i = 1; i <= maxValue; ++i)
            cnt[1][i] = 1;

        for (int len = 2; len < 20; ++len) {
            for (int i = 1; i <= maxValue; ++i) {
                for (int j = i * 2; j <= maxValue; j += i) {
                    cnt[len][j] = (cnt[len][j] + cnt[len - 1][i]) % MOD;
                }
            }
        }

        long res = 0;
        for (int len = 1; len < 20; ++len) {
            long sum = 0;
            for (int v = 1; v <= maxValue; ++v) {
                sum = (sum + cnt[len][v]) % MOD;
            }
            res = (res + sum * comb[n - 1][len - 1]) % MOD;
        }

        return (int) res;
    }
}
