
class Solution:
    def countSubstrings(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def isPalindrome(start, end):
            if start >= end:
                return True

            if s[start] != s[end]:
                return False
            else:
                return isPalindrome(start+1, end-1)

        substr_cnt = 0

        for end in range(0, len(s)):
            for start in range(0, end+1):
                if isPalindrome(start, end):
                    substr_cnt += 1

        return substr_cnt