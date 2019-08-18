"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string
    containing only letters a-z or "." 
    A "." means it can represent any one letter.


Example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

"""

class TrieNode:
    def __init__(self):
        self.children = {}        
        self.hasValue = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                newNode = TrieNode()
                curr.children[key] = newNode
                curr = newNode
        
        curr.hasValue = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, subword):
            curr = node
            for index, key in enumerate(subword):
                if key == '.':
                    # wildcard match
                    for subKey in curr.children:
                        newStart = curr.children[subKey]
                        if dfs(newStart, subword[index+1:]):
                            return True
                    # enumerate all possibilities, no solution
                    return False
                else:
                    if key in curr.children:
                        curr = curr.children[key]
                    else:
                        return False
            # reach the desired node
            return curr.hasValue
        
        # kick off the recursion
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)