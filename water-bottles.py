class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drank = 0
        while numBottles:
            drank += 1
            empty += 1
            numBottles -= 1
            if empty == numExchange:
                empty -= numExchange
                numBottles += 1
        return drank
