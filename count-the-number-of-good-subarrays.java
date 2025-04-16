class Solution {
    public long countGood(int[] nums, int k) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            for(int j=i;j<nums.length;j++){
                if(isGood(nums,i,j,k)){
                    count++;
                }
            }
        }return count;
    }
    public static boolean isGood(int[] arr, int start, int end, int k){
        int count = 0;
        for(int i = start;i<end;i++){
            for(int j = i+1;j<=end;j++){
                if(arr[i]==arr[j])
                    count++;
            }
        }return count>=k;
    }
}
