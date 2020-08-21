class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """ Time Limit Exceed solution """
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        
        @lru_cache(maxsize=None)
        def backtrack(curr, comb):
            if curr == len(nums):
                return all([s == target for s in comb])
            
            comb_list = list(comb)
            for index, subset_sum in enumerate(comb_list):
                if subset_sum + nums[curr] > target:
                    continue
                    
                comb_list[index] += nums[curr]
                if backtrack(curr+1, tuple(sorted(comb_list, reverse=True))):
                    return True
                comb_list[index] -= nums[curr]
            
            return False
        
        nums.sort()
        if nums[-1] > target: return False
        
        comb = [0] * k
        return backtrack(0, tuple(comb))
            