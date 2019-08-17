"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

"""

class TrieNode:
    def __init__(self, key: str) -> None:
        self.key = key
        self.children = {}
        # we don't need to store the actual value, 
        #   since the prefix would do the comparison of values along the path.
        self.hasValue = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # create the new node
                newNode = TrieNode(key)
                curr.children[key] = newNode
                curr = newNode
        
        # reach the desired node
        curr.hasValue = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for key in word:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # mismatch of prefix, early return
                return False
        
        # check if the node contains a value
        return curr.hasValue
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for key in prefix:
            if key in curr.children:
                curr = curr.children[key]
            else:
                # mismatch of prefix, early return
                return False

        # reach the desired node that with the given prefix
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)