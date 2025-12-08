class Solution {
    public int countTriples(int n) {
        int ans = 0;
        for(int i = 1; i <= n; i++) {
            for(int j = i; j <= n; j++) {
                int sum = i*i + j*j;
                int k = (int)Math.sqrt(sum);
                if(k <= n && k*k == sum) ans += 2;
            }
        }   
        return ans;
    }
}
