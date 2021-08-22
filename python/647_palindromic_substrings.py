
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


class Solution:
    def countSubstrings(self, s: str) -> int:

        str_len = len(s)

        def countPalindromicSubstr(start, end):
            cnt = 0
            # expand towards two ends
            while start >= 0 and end < str_len:
                if s[start] != s[end]:
                    break
                start -= 1
                end += 1
                cnt += 1

            return cnt

        total_cnt = 0
        for center in range(0, str_len):
            total_cnt += countPalindromicSubstr(center, center)
            total_cnt += countPalindromicSubstr(center, center+1)

        return total_cnt
