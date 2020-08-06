class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums) + 1)
        dp[0] = float('-inf')
        
        for i, num in enumerate(nums):
            dp[i+1] = max(dp[i]+num, num)
        
        return max(dp)


class SolutionSlidingWindow:
    def maxSubArray(self, nums: List[int]) -> int:
                
        prev_sum, next_sum, max_sum = float('-inf'), 0, float('-inf')
        
        for num in nums:    
            next_sum = max(prev_sum + num, num)
            prev_sum = next_sum
            max_sum = max(max_sum, next_sum)
            
        return max_sum
