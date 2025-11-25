class Solution {
    public int smallestRepunitDivByK(int k) {
        if(k%2==0||k%5==0) return -1;// when k is even and multiple of 5 there is no possible solution 
        
        int count=1,n=1;
        while(n%k!=0){
            n=(n*10+1)%k;//%k is for handling large number of one's
            count++;
        }
        return count;
    }
}
