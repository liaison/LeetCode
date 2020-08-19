class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        results = []
        
        def backtrack(curr, comb):
            
            if curr == len(S):
                results.append("".join(comb))
                return
            
            # branch 1). make the change
            letter = S[curr]
            if letter.isalpha():
                if letter.isupper():
                    comb.append(S[curr].lower())
                else:
                    comb.append(S[curr].upper())
                backtrack(curr+1, comb)
                # backtrack to prepare for the branch 2
                comb.pop()
            
            # branch 2). do not make the change to the ltter
            # either a number or alphabet
            comb.append(S[curr])
            backtrack(curr+1, comb)
            comb.pop()

        backtrack(0, [])

        return results
