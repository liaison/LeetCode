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



class Solution_TLE:
    """
        solution that exceeds the time limit with the following test case:
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)

        dp = [[]] * (len(s)+1)
        dp[0] = [""]

        for endIndex in range(1, len(s)+1):
            sublist = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())

            dp[endIndex] = sublist

        return dp[len(s)]

    
class Solution_Stops:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        
        wordSet = set(wordDict)
        
        dp = [[]] * (len(s)+1)
        dp[0] = [[0]]
        
        for endIndex in range(1, len(s)+1):
            stops = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        copy = subsentence.copy()
                        copy.append(endIndex)
                        stops.append(copy)
            
            print(endIndex, stops)
            
            dp[endIndex] = stops
        
        ret = []
        for stops in dp[len(s)]:
            words = []
            for i in range(len(stops)-1):
                words.append(s[stops[i]:stops[i+1]])
            ret.append(" ".join(words))
        
        return ret


class Solution_RecursiveEncoding:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # quick check 
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        
        wordSet = set(wordDict)
        
        dp = [[]] * (len(s)+1)
        dp[0] = [[0]]
        
        for endIndex in range(1, len(s)+1):
            stops = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    stops.append([startIndex, endIndex])
            dp[endIndex] = stops
        
        ret = []
        def wordDFS(sentence, dp_index):
            if dp_index == 0:
                ret.append(" ".join(sentence))
                return
        
            for start, end in dp[dp_index]:
                word = s[start:end]
                wordDFS([word] + sentence, start)
        
        wordDFS([], len(s))
        
        return ret

    
    
    