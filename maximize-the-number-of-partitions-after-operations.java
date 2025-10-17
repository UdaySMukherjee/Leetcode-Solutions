class Solution {
    public int maxPartitionsAfterOperations(String s, int k) {
        if (k == 26)
            return 1;
        int n = s.length();
        char[] cs = s.toCharArray();
        int[] postCt = new int[n];
        int[] postMk = new int[n];
        int[] postMkt = new int[n];

        int pst = 1, mark = 0, pmkt = 0;
        for (int i = n - 1; i >= 0; i--) {
            int ci = cs[i] - 'a';
            if (!isMark(mark, ci))
                mark |= 1 << ci;
            else
                pmkt |= 1 << ci;
            if (Integer.bitCount(mark) == k + 1) {
                pst++;
                mark = 1 << ci;
                pmkt = 0;
            }
            postCt[i] = pst;
            postMk[i] = mark;
            postMkt[i] = pmkt;
        }
        int res = pst;
        int mkt = 0;
        mark = 0;
        int pc = 0;
        for (int i = 0; i < n; i++) {
            int ci = cs[i] - 'a';

            if (!isMark(mark, ci))
                mark |= 1 << ci;
            else
                mkt |= 1 << ci;

            if (Integer.bitCount(mark) == k + 1) {
                mark = 1 << ci;
                mkt = 0;
                pc++;
            }
            if (Integer.bitCount(mark) == k) {
                if ((Integer.bitCount(mkt) > 0))
                    res = Math.max(res, pc + 1 + postCt[i]);
                if (isMark(mkt, ci) && isMark(postMkt[i], ci) && Integer.bitCount(postMk[i]) == k && Integer.bitCount(mark | postMk[i]) < 26)
                    res = Math.max(res, pc + 2 + postCt[i]);
            }
        }

        return res;
    }

    public boolean isMark(int x, int idx) {
        return (x >> idx & 1) == 1;
    }
}

 
