class Solution {
    public int minimumDeletions(String word, int k) {
        int[] f = new int[26];
        
        for (char c : word.toCharArray()) {
            f[c - 'a']++;
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < 26; i++) {
            if (f[i] == 0) continue;
            int del = 0;
            int cur = f[i];

            for (int j = 0; j < 26; j++) {
                if (f[j] < cur) {
                    del += f[j];
                } else if (Math.abs(f[j] - cur) > k) {
                    del += Math.abs(f[j] - cur) - k;
                }
            }

            ans = Math.min(ans, del);
        }
        return ans;
    }
}
