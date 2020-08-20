class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(ss):
            if len(ss) == 1: return True
            ss_size = len(ss)
            for i in range(ss_size//2):
                if ss[i] != ss[ss_size-i-1]:
                    return False
            return True
        
        results = []
        
        def backtrack(curr, comb):
            if curr == len(s):
                results.append(list(comb))
                return
            
            for end in range(curr+1, len(s)+1):
                substr = s[curr:end]
                if isPalindrome(substr):
                    comb.append(substr)
                    backtrack(curr + len(substr), comb)
                    comb.pop()
        
        backtrack(0, [])
        
        return results