class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = len(prices)
        dp = [0] * (L + 2)

        for buy in range(L-1, -1, -1):
            max_profit = 0
            for sell in range(buy+1, L):
                profit = (prices[sell] - prices[buy]) + dp[sell+2]
                max_profit = max(profit, max_profit)
            
            # In addition, we need to compare with doing no transaction
            dp[buy] = max(max_profit, dp[buy+1])

        return dp[0]
