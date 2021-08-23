class Solution:
    def rob(self, nums: List[int]) -> int:

        to_rob, not_to_rob = 0, 0

        # state machine
        # At each step, we calculate profits of two choices: to_rob, not_to_rob
        for num in nums:
            # if we break down into two statements,
            #  we need some temporary values to ensure the same results.
            to_rob, not_to_rob = max(not_to_rob + num, to_rob), max(to_rob, not_to_rob)

        return max(to_rob, not_to_rob)


class Solution:
    def rob(self, nums: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dfs(start, accu):

            if start >= len(nums):
                return accu

            return max(dfs(start+1, accu), dfs(start+2, accu + nums[start]))

        return dfs(0, 0)