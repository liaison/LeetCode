class Solution:
    def minCut(self, s: str) -> int:
        
        # element indicates the minimal number of partitions
        #  we need to divide the corresponding substring
        dp = [0] * (len(s)+1)
        
        for right in range(1, len(s)+1):
            num_parts = float('inf')
            
            for left in range(0, right):
                substr = s[left:right]
                # isPalindrome(s[left:right])
                if substr == substr[::-1]:   
                    num_parts = min(num_parts, dp[left]+1)
                    if left == 0:
                        # cannot have less than one partition
                        break
                        
            dp[right] = num_parts
        
        return dp[len(s)] - 1
