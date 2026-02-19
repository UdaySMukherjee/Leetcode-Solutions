class Solution {
    public int countBinarySubstrings(String s) {
        int n = s.length(), i = 0, ans = 0;
        ArrayList<Integer> arr = new ArrayList<>();

        while (i < n) {
            char ch = s.charAt(i);
            int count = 0;

            while (i < n && s.charAt(i) == ch) {
                count++;
                i++;
            }

            arr.add(count);
        }

        for (int j = 1; j < arr.size(); j++) {
            ans += Math.min(arr.get(j), arr.get(j - 1));
        }

        return ans;
    }
}
