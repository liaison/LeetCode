class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # maximum sum of postfix that ends with nums[i]
        dp = [0] * (len(nums) + 1)
        dp[0] = float('-inf')

        for i, num in enumerate(nums):
            dp[i+1] = max(dp[i]+num, num)

        # maximum postfixes of all, i.e. maximum subarray
        return max(dp)


class SolutionSlidingWindow:
    def maxSubArray(self, nums: List[int]) -> int:

        prev_sum, next_sum, max_sum = float('-inf'), 0, float('-inf')

        # approach with state machine
        for num in nums:
            next_sum = max(prev_sum + num, num)
            prev_sum = next_sum
            max_sum = max(max_sum, next_sum)

        return max_sum


class SolutionExactSubarray:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [(0, 0)] * (len(nums)+1)
        # (max subarray sum sofar, starting index of subarray)
        dp[0] = (float('-inf'), -1)

        for index, num in enumerate(nums):

            prev_sum, prev_index = dp[index]

            if num > prev_sum + num:
                dp[index+1] = (num, index)
            else:
                dp[index+1] = (prev_sum + num, prev_index)

        # for a follow-up question:
        # return the max sum as well as the exact subarray
        max_sum, start_index = max(dp, key=lambda x:x[0])

        return max_sum