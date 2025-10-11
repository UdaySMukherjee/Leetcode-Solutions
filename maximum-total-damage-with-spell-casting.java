import java.util.*;

class Solution {
    public long maximumTotalDamage(int[] power) {
        if (power.length == 0) return 0;

        Arrays.sort(power);
        List<Integer> vals = new ArrayList<>();
        List<Long> earn = new ArrayList<>();

        for (int i = 0; i < power.length; ) {
            int v = power[i];
            long sum = 0;
            while (i < power.length && power[i] == v) {
                sum += v;
                i++;
            }
            vals.add(v);
            earn.add(sum);
        }

        int n = vals.size();
        long[] dp = new long[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            int nextIdx = Collections.binarySearch(vals, vals.get(i) + 3);
            if (nextIdx < 0) nextIdx = -nextIdx - 1;
            long take = earn.get(i) + dp[nextIdx];
            long skip = dp[i + 1];
            dp[i] = Math.max(take, skip);
        }

        return dp[0];
    }
}
