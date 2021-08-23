
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




