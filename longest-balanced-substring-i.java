class Solution {
    public int longestBalanced(String s) {
        int len = s.length();
        int maxLength = 0;

        for (int i = 0; i < len; i++) {

            // 0th index represents the count of char 'a' , 1th index -> count of char 'b' and so on....
            int[] charCount = new int[26];
            for (int j = i; j < len; j++) {

                charCount[s.charAt(j) - 'a']++;

                // traversing the charCount array to check if the balanced condition is still valid
                boolean isBalanced = true;
                for (int k = 0; k < 26; k++) {
                    // 0 charCount means the character hasnt appeared yet in current substring
                    if (charCount[k] != 0 && charCount[s.charAt(j) - 'a'] != charCount[k]) {
                        isBalanced = false;
                        break;
                    }
                }

                if (isBalanced == true)
                    maxLength = Math.max(maxLength , j-i+1);

            }

        }

        return maxLength;
    }
}
