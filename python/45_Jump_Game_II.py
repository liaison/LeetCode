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


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            Greedy scanning with the sliding window
        """
        if len(nums) < 2:
            # no need to jump
            return 0
        
        next_scope = nums[0]
        curr_reach = nums[0]
        
        # starting from a simple jump
        jumps = 1
        
        for curr, steps in enumerate(nums):
            
            # when the index exceeds the reaching window
            if curr > curr_reach:
                jumps += 1
                # we jump to the maximum distance thanks to the sliding window
                curr_reach = next_scope
            
            # sliding window to extend the scope of the reach
            next_scope = max(next_scope, curr + steps) 
    
    
        return jumps