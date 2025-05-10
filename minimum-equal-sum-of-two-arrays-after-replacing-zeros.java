class Solution {
    public long minSum(int[] nums1, int[] nums2) {
        long[] result1 = calculateSumAndZeroCount(nums1);
        long[] result2 = calculateSumAndZeroCount(nums2);
        
        long total1 = result1[0] + result1[1];
        long total2 = result2[0] + result2[1];
        
        if (total1 == total2) {
            return total1;
        }
        
        long[] smallerResult = total1 < total2 ? result1 : result2;
        long[] largerResult = (smallerResult == result1 ? result2 : result1);
        
        return smallerResult[1] == 0 ? -1 : largerResult[0] + largerResult[1];
    }

    private long[] calculateSumAndZeroCount(int[] nums) {
        long[] sumAndZeroCount = {0, 0}; // [sum, zeroCount]
        for (int num : nums) {
            if (num == 0) {
                sumAndZeroCount[1]++;
            }
            sumAndZeroCount[0] += num;
        }
        return sumAndZeroCount;
    }
}
