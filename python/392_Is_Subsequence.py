class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        LEFT_BOUND = len(s)
        RIGHT_BOUND = len(t)
        
        @lru_cache(None)
        def rec_isSubsequence(left_index, right_index):
            if left_index == LEFT_BOUND:
                return True
            elif right_index == RIGHT_BOUND:
                return False
            
            if s[left_index] == t[right_index]:
                left_index += 1
                right_index += 1
            else:
                right_index += 1
            
            return rec_isSubsequence(left_index, right_index)
        
        
        return rec_isSubsequence(0, 0)