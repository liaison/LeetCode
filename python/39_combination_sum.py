class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        global_set = []
        
        def comb_to_list(comb):
            ret = []
            for index, count in enumerate(comb):
                if count > 0:
                    ret.extend([candidates[index]]*count)
            return ret
            
        @lru_cache(maxsize=None)
        def dfs(remain, comb):
            
            if remain == 0:
                global_set.append(comb_to_list(comb))
                return
            
            for index, candidate in enumerate(candidates):
                if remain >= candidate:
                    new_comb = list(comb)
                    new_comb[index] += 1
                    dfs(remain - candidate, tuple(new_comb))
            
        comb = tuple([0] * len(candidates))
        dfs(target, comb)
        
        return global_set

    
class SolutionBT:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
