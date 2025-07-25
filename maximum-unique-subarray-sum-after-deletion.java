import java.util.Arrays;

class Solution {
    public int maxSum(int[] numbers) {
        Arrays.sort(numbers); // 🔃 Step 1: Sort the array
        int previous = numbers[numbers.length - 1]; // Largest number
        int result = previous; // Initialize result with largest
        for (int index = numbers.length - 2; index >= 0; index--) {
            int currentValue = numbers[index];
            if (currentValue <= 0) return result; // 🚫 Stop at zero or negative
            if (currentValue != previous) result += currentValue; // ✅ Add if unique
            previous = currentValue; // Update previous
        }
        return result; // 🎯 Return final result
    }
}
