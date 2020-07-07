class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        # knapsack problem
        # each rod to be placed in either left or right bin, or discarded
        # find the maximum sum of postive numbers, with the total sum of zero
        dp = {}
        # dp[sum] = max_sum_of_postive_number (left bin)
        dp[0] = 0
        for rod in rods:
            
            newDP = defaultdict(int)
            for rodSum in dp:
                newDP[rodSum] = max(dp[rodSum], newDP[rodSum])
                newDP[rodSum + rod] = max(dp[rodSum] + rod, newDP[rodSum + rod])
                newDP[rodSum - rod] = max(dp[rodSum], newDP[rodSum - rod])
            
            dp = newDP
        
        return dp[0]
