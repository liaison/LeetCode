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