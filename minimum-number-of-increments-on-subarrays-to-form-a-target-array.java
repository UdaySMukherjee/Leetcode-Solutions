class Solution {
    public int minNumberOperations(int[] target) {
        int previous = 0;
        int result = 0;

        for (int num: target) {
            if (num > previous) {
                result += num - previous;
            }

            previous = num;
        }

        return result;
    }
}
