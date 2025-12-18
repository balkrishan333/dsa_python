from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        days = len(prices)
        # Initialize as nested lists        
        dp = [[[0 for _ in range(3)] for _ in range(k + 1)] for _ in range(days)]
        
        # Step 1 - Initialize DP array
        for tx in range(k + 1):
            dp[0][tx][0] = 0
            dp[0][tx][1] = -prices[0]
            dp[0][tx][2] = prices[0]

        for day in range(1, days):
            for tx in range(1, k + 1):
               dp[day][tx][0] = max(dp[day-1][tx][0], dp[day-1][tx][1] + prices[day], dp[day-1][tx][2] - prices[day])
               dp[day][tx][1] = max(dp[day-1][tx][1], dp[day - 1][tx-1][0] - prices[day])
               dp[day][tx][2] = max(dp[day-1][tx][2], dp[day - 1][tx-1][0] + prices[day])
        
        return dp[days - 1][k][0]
        

sln = Solution()
print(sln.maximumProfit(prices=[1,7,9,8,2], k=2))