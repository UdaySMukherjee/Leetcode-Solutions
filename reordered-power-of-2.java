class Solution {
    public boolean reorderedPowerOf2(int n) {
        int[] nArr = getDigit(n);

        for (int i = 0; i < 31; i++) {
            int power = 1 << i;
            int[] powerArr = getDigit(power);

            if (Arrays.equals(nArr, powerArr)) return true;
        }

        return false;
    }

    public int[] getDigit(int num) {
        int[] arr = new int[10];
        while (num > 0) {
            int digit = num % 10;
            arr[digit]++;
            num /= 10;
        }
        return arr;
    }
}
