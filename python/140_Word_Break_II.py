"""
Given a non-empty string s and a dictionary wordDict 
containing a list of non-empty words, add spaces in s to 
construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
    [
      "cats and dog",
      "cat sand dog"
    ]
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        from collections import defaultdict

        memo = defaultdict(list)
        
        def DFS(s):
            """ top-down DFS with memoization """"
            #nonlocal memo
            if not s:
                return [None]
            
            if s in memo:
                return memo[s]
            
            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    for sentence in DFS(s[endIndex:]):
                        memo[s].append(word + (' ' + sentence if sentence else ''))
            
            return memo[s]
        
        DFS(s)
        return memo[s]
