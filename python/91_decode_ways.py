"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).


Note:
    there are a few "exceptional" test cases, such as '0', '101' and '01' that one should takes into account.

"""

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.count(s)

    @lru_cache(maxsize=None)
    def count(self, s):
        """ recursion with memoization
        """
        if len(s) == 0:
            return 1
        
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return self.count(s[1:])
        if len(s) >= 2:
            if int(s[0:2]) < 27:
                return self.count(s[1:]) + self.count(s[2:])
            else:
                return self.count(s[1:])
        
