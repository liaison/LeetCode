class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = dict()
        trie["$"] = ""  # pseudo mark

        def update_trie(word, trie):
            """ Update the Trie structure with a new word """
            for letter in word:
                if letter not in trie:
                    trie[letter] = dict()
                trie = trie[letter]
            # mark the end of word
            trie["$"] = word

        for word in words:
            update_trie(word, trie)

        max_word = ""
        def dfs(node):
            """
                Traverse the Trie (as Tree) to find the deepest/longest word
            """
            nonlocal max_word

             # missing a match of word at this prefix
            if "$" not in node:
                return

            if len(node["$"]) > len(max_word):
                max_word = node["$"]
            elif len(node["$"]) == len(max_word) and node["$"] < max_word:
                max_word = node["$"]

            for key in node.keys():
                if key != "$":
                    dfs(node[key])

        dfs(trie)

        return max_word


