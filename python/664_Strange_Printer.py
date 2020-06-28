"""
    Reference: https://leetcode.com/problems/strange-printer/discuss/106810/Java-O(n3)-DP-Solution-with-Explanation-and-Simple-Optimization
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        str_size = len(s)
        if str_size == 0:
            return 0
        
        # init with the value 'n', size of the square
        dp = [[str_size]*str_size for i in range(str_size)]
        for i in range(str_size):
            # reset the diagnoal values
            dp[i][i] = 1
        
        # complexity O(N^3)
        for end in range(0, str_size):
            for start in range(end, -1, -1):
                for mid in range(start, end):
                    default_print_num = dp[start][mid] + dp[mid+1][end]
                    if s[mid] == s[end]:
                        default_print_num -= 1
                    dp[start][end] = min(dp[start][end], default_print_num)
        
        
        return dp[0][str_size-1]