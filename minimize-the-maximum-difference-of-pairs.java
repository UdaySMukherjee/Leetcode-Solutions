class Solution {
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        return binarySearch(nums, p);
    }

    private boolean canFormPairs(int[] nums, int d, int p) {
        int c = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i + 1] - nums[i] <= d) {
                c++;
                i++;
            }
            if (c >= p) return true;
        }
        return false;
    }

    private int binarySearch(int[] nums, int p) {
        int L = 0, H = nums[nums.length - 1] - nums[0];
        while (L < H) {
            int M = L + ((H - L) >> 1);
            if (canFormPairs(nums, M, p)) {
                H = M;
            } else {
                L = M + 1;
            }
        }
        return L;
    }

    
}
