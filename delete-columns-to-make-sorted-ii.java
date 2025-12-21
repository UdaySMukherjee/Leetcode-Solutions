class Solution {
    public int minDeletionSize(String[] strs) {
        int n = strs[0].length();
        int m = strs.length;
        int noOfDeletions = 0;
        
        // Track which adjacent pairs are already in definite order
        boolean[] sorted = new boolean[m - 1];

        for (int i = 0; i < n; i++) {
            // Tentatively assume this column will be kept
            boolean[] temp = sorted.clone();
            boolean deleteColumn = false;

            // Check each adjacent pair of strings
            for (int j = 0; j < m - 1; j++) {
                if (!sorted[j]) { // Only check unsettled pairs
                    if (strs[j].charAt(i) > strs[j + 1].charAt(i)) {
                        // Violation found - must delete this column
                        deleteColumn = true;
                        break;
                    } 
                    else if(strs[j].charAt(i) < strs[j + 1].charAt(i)) {
                        // This pair is now settled by current column
                        temp[j] = true; 
                    }
                }
            }

            if (deleteColumn) {
                noOfDeletions++;
            }
            else{
                // Column kept - commit the settlements
                sorted = temp;
            }
        }

        return noOfDeletions;
    }
}
