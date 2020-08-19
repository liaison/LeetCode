class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        def backtrack(start, comb):
            if start == len(nums):
                results.append(list(comb))
                return results
            # binary tree branches
            # take the current number into subset or not
            backtrack(start+1, comb + [nums[start]])
            backtrack(start+1, comb)
        
        backtrack(0, [])
        
        return results


class SolutionBacktrack:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        def backtrack(curr, comb):
            if curr == len(nums):
                results.append(list(comb))
                return results
            # binary tree branches
            # take the current number into subset or not
            comb.append(nums[curr])
            backtrack(curr+1, comb)
            comb.pop()
            backtrack(curr+1, comb)
        
        backtrack(0, [])
        
        return results