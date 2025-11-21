class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];

        // initialize
        Arrays.fill(first, -1);
        Arrays.fill(last, -1);

        // find first and last occurrences
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        int ans = 0;

        // check for each character a-z
        for (int ch = 0; ch < 26; ch++) {
            if (first[ch] == -1 || first[ch] == last[ch]) continue;

            boolean[] seen = new boolean[26];
            for (int i = first[ch] + 1; i < last[ch]; i++) {
                seen[s.charAt(i) - 'a'] = true;
            }

            // count distinct mid characters
            int cnt = 0;
            for (boolean b : seen) if (b) cnt++;

            ans += cnt;
        }

        return ans;
    }
}
