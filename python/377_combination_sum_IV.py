class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        """
            dynamic programming:
                comb[target] = sum(comb[target-nums[i]])

               - treat each candidate number as the last number in the final combination.
               - append the candidate number to the combinations of (target - nums[i]), i.e. comb[target-nums[i]]
        """
    
        #import functools
        @functools.lru_cache(maxsize = None)
        def combinationSum4(remain):
            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combinationSum4(remain - num)
            return result

        return combinationSum4(target)
