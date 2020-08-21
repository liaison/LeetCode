class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        @lru_cache(maxsize=None)
        def backtrack(curr, curr_sum):

            if curr_sum == target:
                return True
            elif curr_sum > target or curr == len(nums):
                return False
            
            if backtrack(curr+1, curr_sum + nums[curr]):
                return True
            
            if backtrack(curr+1, curr_sum):
                return True
        
        return backtrack(0, 0)
