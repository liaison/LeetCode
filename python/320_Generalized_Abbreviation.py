class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        results = []
        
        def backtrack(curr, comb, is_abbr):
            
            if curr == len(word):
                results.append("".join(comb))
                return
            
            if is_abbr:
                # when the abbreviation is permitted
                # we could decide to do it or NOT
                length = len(word) - curr
                for s in range(1, length+1):
                    comb.append(str(s))
                    backtrack(curr+s, comb, False)
                    comb.pop()
                
                # not doing abbreviation
                comb.append(word[curr])
                backtrack(curr+1, comb, True)
                comb.pop()
                
            else:
                # we cannot have two abbreviations in a row
                comb.append(word[curr])
                backtrack(curr+1, comb, True)
                comb.pop()
        
        backtrack(0, [], True)
        
        return results
