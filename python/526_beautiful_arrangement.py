class Solution:
    def countArrangement(self, N: int) -> int:
        
        nums = [i+1 for i in range(N)]
        comb_count = 0
        def backtrack(start, comb):
            nonlocal comb_count

            if start == N:
                comb_count += 1
                return

            for index in range(start, N):

                if (start + 1) % nums[index] == 0 \
                    or nums[index] % (start + 1) == 0:
                    # mark the choice
                    comb[start], comb[index] = comb[index], comb[start]
                    backtrack(start+1, comb)
                    # revert the choice    
                    comb[start], comb[index] = comb[index], comb[start]         
        
        backtrack(0, nums)

        return comb_count
