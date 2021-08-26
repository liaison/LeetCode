
class SolutionDP:
    def longestPalindrome(self, s: str) -> str:

        """
            with memoization/dp, this solution still runs into TLE.
        """
        @functools.lru_cache(maxsize=None)
        def isPalindrome(start, end):
            if start >= end:
                return True

            if s[start] == s[end]:
                return isPalindrome(start+1, end-1)
            else:
                return False

        for substr_size in range(len(s), 0, -1):
            for start in range(0, len(s) - substr_size + 1):
                end = start + substr_size - 1
                if isPalindrome(start, end):
                    return s[start:(end+1)]


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def extend_around_center(left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            # return the length of palindrome string
            return (right - left - 1)

        max_start, max_end = 0, 0

        for index in range(len(s)):
            len1 = extend_around_center(index, index)
            len2 = extend_around_center(index, index+1)

            max_len = max(len1, len2)
            if max_len > (max_end - max_start):
                max_start = index - (max_len-1) // 2
                max_end = index + max_len // 2

        return s[max_start:(max_end+1)]


