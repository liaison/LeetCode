"""
Given a non-empty string s and a dictionary wordDict containing
a list of non-empty words, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
"""


# ====================================================================

class SolutionDP(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]

        # start of the dynamic programming solution.
        dp[0] = True

        # dp[endIndex]: indicates the viability of substring s[0:endIndex]

        # endIndex marks the end of the substring to check
        for endIndex in range(1, len(s)+1):
            # Check the viability of substring, using the previous intermediate results.
            #for beginIndex in range(0, i):
            # We could have some speedup if we check the word from the end of the string,
            #   since the new word might appear when the string grows.
            for beginIndex in reversed(range(0, endIndex)):

                if dp[beginIndex] and s[beginIndex:endIndex] in wordDict:
                    dp[endIndex] = True
                    break

        return dp[len(s)]

# ====================================================================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.keySet = set()

    def insert(self, word):
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                newNode = TrieNode()
                curr.children[key] = newNode
                curr = newNode

            self.keySet.add(key)

        curr.isWord = True

    def containsKey(self, key):
        """ Check if the Trie contains the letter/key """
        return key in self.keySet

    def getRoot(self):
        return self.root

    def match(self, word):
        """ Not necessary in this problem """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # no match at all
                return 0

        return 2 if curr.isWord else 1


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # construct a word Trie
        wordTrie = Trie()
        for word in wordDict:
            wordTrie.insert(word)

        rootTrieNode = wordTrie.getRoot()

        # Additional quick check, before jumping into recursion.
        for i in range(len(s)-1, 0, -1):
            if not wordTrie.containsKey(s[i]):
                return False

        # memoization
        memo = {} # len(s): dfs result

        def dfs(trieNode, s):
            """
                DFS recursion with memoization.
                Note: we should store all the intermediates results in all exits/returns.
            """
            nonlocal rootTrieNode
            nonlocal memo

            if s == '':
                return True

            if len(s) in memo:
                return memo[len(s)]

            currTrieNode = trieNode
            for index, c in enumerate(s):
                if c not in currTrieNode.children:
                    # Important to store all the intermediate results.
                    memo[len(s)] = False
                    return False
                else:
                    currTrieNode = currTrieNode.children[c]

                if currTrieNode.isWord:
                    #print(s[index+1:])
                    if dfs(rootTrieNode, s[index+1:]):
                        memo[len(s)-index-1] = True
                        return True

            memo[len(s)] = False
            return False


        return dfs(rootTrieNode, s)



class SolutionMemoDFS:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        limit = len(s)

        @cache
        def memo_dfs(start_index):
            """
                function to determine if we can find the match for the substring starting from `start_index`
            """
            if start_index == limit:
                # match the end of the string
                return True

            for end_index in range(start_index+1, limit+1):
                substr = s[start_index:end_index]
                if substr in word_set:
                    # one candidate word match, continue the search
                    if memo_dfs(end_index):
                        return True
            return False

        return memo_dfs(0)







