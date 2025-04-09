class Solution {
    public int minOperations(int[] nums, int k) {
        Set<Integer> storage = new HashSet<>();
        int result=0;

        for(int num: nums){
            if(!storage.contains(num)){
                storage.add(num);

                if(num>k){
                    result++;
                }
                else if(num<k){
                    return -1;
                }
            }
            
        }

        return result; 
    }
}
