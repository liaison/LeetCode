class Solution:
    def jump(self, nums: List[int]) -> int:
        """ TLE (Time Limit Exceeded) """
        end = len(nums)
        
        @lru_cache(maxsize=None)
        def backtrack(curr):
            
            steps = end - curr - 1
            if nums[curr] >= steps:
                return 0 if end == 1 else 1
            
            min_jumps = float('inf')
            for next_step in range(curr+1, min(curr+nums[curr]+1, end)):
                min_jumps = min(min_jumps, 1 + backtrack(next_step))
            
            return min_jumps
        
        return backtrack(0)