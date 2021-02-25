class SolutionTLE:
    def longestPalindromeSubseq(self, s: str) -> int:

        max_len = 0
        str_len = len(s)

        def dfs(index, subsequence):
            nonlocal max_len

            if subsequence == subsequence[::-1]:
                max_len = max(max_len, len(subsequence))

            if index == str_len:
                return

            dfs(index+1, subsequence)
            dfs(index+1, subsequence + s[index])


        dfs(0, "")

        return max_len


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        """
            optimized break-down of the problem,
            with less memory consumption, as well as less computation.
        """
        @functools.lru_cache(maxsize=None)
        def dp(left, right):

            if left == right:
                return 1
            elif left > right:
                return 0

            if s[left] == s[right]:
                return 2 + dp(left+1, right-1)
            else:
                return max(dp(left+1, right), dp(left, right-1))

        return dp(0, len(s)-1)