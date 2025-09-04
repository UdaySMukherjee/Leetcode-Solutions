class Solution {
    public int findClosest(int x, int y, int z) {
        int a = Math.abs(x - z), b = Math.abs(y - z);
        return ((a > b) ? 2 : 0) | ((a < b) ? 1 : 0);
    }
}
