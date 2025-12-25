class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        long result = 0;
        int n = happiness.length;
        
        Arrays.sort(happiness);
        
        for(int i = 0; i < n / 2; i++) {
            int temp = happiness[n - 1 - i];
            happiness[n - 1 - i] = happiness[i];
            happiness[i] = temp;
        }

        for(int i = 0; i < k; i++) {
            result += Math.max(0, happiness[i]);
            decrement_ops(happiness, i + 1);
            
        }

        return result;
    }

    public void decrement_ops(int[] inputArray, int index) {
        for(int i = index; i < inputArray.length; i++) {
            if(inputArray[i] > 0) {
                inputArray[i] -= 1;
            }
        }
    }
}
