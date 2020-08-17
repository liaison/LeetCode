"""

You are given coins of different denominations and a total amount of money.

Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount+1)
        dp[0] = 1
        
        # the order of the nested loop is essential!
        # won't work if we switch the order.
        # e.g. for the amount 3, with coins of [1, 2]
        #   3 = 2 + 1
        #   3 = 1 + 2   
        #  would be counted as different combination
        #  if we start with the subamount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[amount]
