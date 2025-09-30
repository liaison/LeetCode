class Solution:

    def linear_rob(self, nums):
        if len(nums) == 0:
            return 0
        size = len(nums)
        dp = [0] * (size+1)
        dp[size-1] = nums[-1]

        #   size-2, size-1, size, size+1
        for index in range(size-2, -1, -1):
            dp[index] = max(
                nums[index] + dp[index+2],
                dp[index+1])

        return dp[0]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # reduce the problem into two subproblems
        #  the subproblem could be solved without the circular constraint
        choice_1 = self.linear_rob(nums[1:])
        choice_2 = self.linear_rob(nums[:-1])

        return max(choice_1, choice_2)