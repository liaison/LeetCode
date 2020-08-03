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