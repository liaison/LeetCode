"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 


Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 


Note:
    - There may be more than one LIS combination, it is only necessary for you to return the length.
    - Your algorithm should run in O(n2) complexity.

Follow up:
    Could you improve it to O(n log n) time complexity?
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        # the longest increasing subsequence for the prefix [0...i]
        dp = [1] * (len(nums))
        
        globalMaxLen = -1
        
        for i, num in enumerate(nums):
            localMaxLen = 1
            for k in range(i):
                if nums[i] > nums[k]:
                    localMaxLen = max(dp[k]+1, localMaxLen)
            
            dp[i] = localMaxLen
            globalMaxLen = max(localMaxLen, globalMaxLen)
            
        return globalMaxLen
