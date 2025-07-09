class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] gaps = new int[n + 1];
        gaps[0] = startTime[0];
        for (int i = 1; i < n; ++i) {
            gaps[i] = startTime[i] - endTime[i - 1];
        }
        gaps[n] = eventTime - endTime[n - 1];
        int sz = Math.min(k + 1, gaps.length);
        long curr = 0, best = 0;
        for (int i = 0; i < sz; ++i) curr += gaps[i];
        best = curr;
        for (int i = sz; i < gaps.length; ++i) {
            curr += gaps[i] - gaps[i - sz];
            if (curr > best) best = curr;
        }
        return (int) best;
    }
}
