class Solution {
    public int countHillValley(int[] nums) {
        List<Integer> v = new ArrayList<>();
        v.add(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                v.add(nums[i]);
            }
        }

        int count = 0;
        for (int i = 1; i < v.size() - 1; i++) {
            int prev = v.get(i - 1);
            int curr = v.get(i);
            int next = v.get(i + 1);

            if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
                count++;
            }
        }
        return count;
    }
}
