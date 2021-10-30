class Trie:

    def __init__(self):
        self.trie = dict()
        # a special character to mark the count of word
        self.word_count = "#"


    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        if self.word_count in node:
            node[self.word_count] += 1
        else:
            node[self.word_count] = 1


    def countWordsEqualTo(self, word: str) -> int:
        node = self.trie
        for char in word:
            if char not in node:
                return 0
            node = node[char]
        if self.word_count in node:
            return node[self.word_count]
        else:
            return 0


    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.trie
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]

        total_words = 0
        def dfs(node):
            nonlocal total_words
            if self.word_count in node:
                total_words += node[self.word_count]
            for next_char in node.keys():
                if next_char != self.word_count:
                    dfs(node[next_char])

        dfs(node)
        return total_words


    def erase(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                return
            node = node[char]

        if self.word_count in node:
            if node[self.word_count] > 0:
                node[self.word_count] -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)


