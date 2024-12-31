class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a set of travel days for quick lookup
        travel_days = set(days)

        # Initialize a DP array for 365 days
        dp = [0] * 366  # dp[i] is the min cost to travel up to day i

        for i in range(1, 366):
            if i not in travel_days:
                # If it's not a travel day, the cost is the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Calculate the cost if we buy a 1-day, 7-day, or 30-day pass
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[max(0, i - 7)] + costs[1]
                cost30 = dp[max(0, i - 30)] + costs[2]
                
                # Take the minimum of the three options
                dp[i] = min(cost1, cost7, cost30)

        # Return the cost to cover all days in the year
        return dp[365]
