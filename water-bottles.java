class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        while(numBottles >= numExchange) {
            ans = ans + (int)(numBottles/numExchange);
            numBottles = (int)(numBottles/numExchange) + (numBottles % numExchange);
        }
        return ans;
    }
}
