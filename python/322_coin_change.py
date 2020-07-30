"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ with memoization, still Time Limit Exceeded """

        @lru_cache(maxsize=None)
        def dfs(sub_amount, count):
            
            if sub_amount == 0:
                return count
            elif sub_amount < 0:
                return -1
            
            min_count = float("inf")
            for coin in coins:
                
                new_count = dfs(sub_amount - coin, count+1)
                if new_count > 0:
                    min_count = min(min_count, new_count)
            
            return -1 if min_count == float("inf") else min_count
                
        
        return dfs(amount, 0)


class SolutionDP:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount+1)
        dp[0] = 0
        for sub_amount in range(1, amount+1):
            
            for coin in coins:
                if sub_amount - coin >= 0:
                    if dp[sub_amount-coin] >= 0:
                        if dp[sub_amount] == -1:
                            dp[sub_amount] = dp[sub_amount-coin] + 1
                        else:
                            dp[sub_amount] = min(
                                dp[sub_amount], dp[sub_amount-coin] + 1)
        
        return dp[amount]