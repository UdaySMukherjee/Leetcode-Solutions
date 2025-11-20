class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] == b[1]) return b[0] - a[0];
            return a[1] - b[1];
        });
        int p1 = -1, p2 = -1; 
        int count = 0;
        for (int[] it : intervals) {
            int s = it[0];
            int e = it[1];
            if (p2 >= s) {
                continue;
            }
            if (p1 >= s) {
                count++;
                p2 = p1;
                p1 = e;
            } else {
                count += 2;
                p2 = e - 1;
                p1 = e;
            }
        }
        return count;
    }
}
