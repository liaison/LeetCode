class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums) + 1)
        dp[0] = float('-inf')
        
        for i, num in enumerate(nums):
            dp[i+1] = max(dp[i]+num, num)
        
        return max(dp)