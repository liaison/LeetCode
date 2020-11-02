class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif (k == 1) and (n >= 3):
            return 0
        
        dp = [0 for i in range(n)]
        dp[0] = k
        dp[1] = k * k
        
        for i in range(2, n):
            # case 1). last two fences of the same colors
            # case 2). last two fences of different colors
            dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)
        
        return dp[-1]
