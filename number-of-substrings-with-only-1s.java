class Solution {
    public int numSub(String s) {
        long ans=0,ones=0;
        for(int i=0;i<s.length();i++) {
            if(s.charAt(i) == '1')
                ones++;
            else {
                ans += (ones*(ones+1)/2);
                ones=0;
            }
        }
        ans += (ones*(ones+1)/2);
        return (int)(ans%1000000007);
    }
}
