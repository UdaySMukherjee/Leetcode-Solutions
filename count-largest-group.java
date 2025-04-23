class Solution {
    public static int sumofDigit(int n){
        int sum=0;
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        return sum;
    }
    public int countLargestGroup(int n) {
        int[] arr = new int[37];
        int count = 0;
        for(int i=1;i<=n;i++){
            arr[sumofDigit(i)]++;
        }
        int maxsum=0;
        for(int i: arr){
            maxsum=Math.max(maxsum,i);
        }
        for(int i: arr){
            if(i==maxsum){
                count++;
            }
        }
        return count;
    }
}
