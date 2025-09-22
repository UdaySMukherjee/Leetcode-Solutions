import java.util.*;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] freq = new int[101];  // numbers are in range 1–100
        for (int num : nums) {
            freq[num]++;
        }

        int maxFreq = 0;
        for (int f : freq) {
            maxFreq = Math.max(maxFreq, f);
        }

        int result = 0;
        for (int f : freq) {
            if (f == maxFreq) {
                result += f;
            }
        }

        return result;
    }
}
