
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        global_set = []
        
        def backtrack(remain, comb, next_start):
            """
                remain: remaining sum
                comb:   the current combination
                next_start: the starting index for the next candidates
                
                Pick the candidates in order, 
                so that we won't have any duplidates
                e.g. if we picked the number 3 in the previous step,
                     then in the following steps,
                       the list of candiates become [4 5, ... 9]
            """
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                global_set.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                comb.pop()
        
        comb = []
        backtrack(n, comb, 0)
        
        return global_set
