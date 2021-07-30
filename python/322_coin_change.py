"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

"""

class Solution:
    def coinChange_greedy_BFS(self, coins: List[int], amount: int) -> int:
        """
            Better than the normal BFS, but still exceed the time limit
        """
        queue = [(0, 0)]
        heapq.heapify(queue)

        # Greedy BFS, similar to find the shortest distance between two nodes in graph
        while queue:
            sub_amount, coin_count = heapq.heappop(queue)

            # the heapq is min queue, rather than max
            sub_amount = abs(sub_amount)

            if sub_amount == amount:
                return coin_count

            for coin in coins:
                new_amount = sub_amount + coin
                if new_amount <= amount:
                    heapq.heappush(queue, (-new_amount, coin_count + 1))

        return -1


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


class SolutionRefinedDP:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # set the 'inf' so that we could use less conditions in the following loop.
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0

        # one could swap the order of the loops
        #   though this order can deal with more scenarios.
        for coin in coins:
            for sub_amount in range(coin, amount+1):
                dp[sub_amount] = min(dp[sub_amount], dp[sub_amount-coin]+1)

        return -1 if dp[amount] == float('inf') else dp[amount]


