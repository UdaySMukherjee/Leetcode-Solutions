class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        startTime = customers[0][0]
        timeSum = 0

        for i in range(len(customers)):
            if startTime < customers[i][0]:
                startTime = customers[i][0]

            time2cook = startTime + customers[i][1]
            timeSum += time2cook - customers[i][0]
            startTime = time2cook

        return float(timeSum) / len(customers)
