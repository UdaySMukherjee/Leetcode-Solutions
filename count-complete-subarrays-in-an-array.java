class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int[] count = new int[2001];
        int n = nums.length;
        int total = 0;
        for(int i:nums){
            count[i]++;
            if(count[i]==1) total++;
        }
        Arrays.fill(count,0);
        int i = 0, c = 0,ans = 0;
        for(int j = 0;j<n;j++){
            count[nums[j]]++;
            if(count[nums[j]]==1) c++;
            while(i<=j && c == total){
                ans += n-j;
                count[nums[i]]--;
                if(count[nums[i]]==0)
                    c--;
                i++;
            }
        }
        return ans;
    }
}
