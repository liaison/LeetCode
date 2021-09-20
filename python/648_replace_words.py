class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = {}

        def update_trie(word, trie):
            for letter in word:
                if letter not in trie:
                    trie[letter] = {}
                trie = trie[letter]
            trie["$"] = word

        # building a Trie data structure for all words
        for word in dictionary:
            update_trie(word, trie)

        def find_min_prefix(word, trie):
            """
                Find the shortest common prefix
            """
            for letter in word:
                if letter not in trie:
                    return ""
                trie = trie[letter]
                if "$" in trie:
                    return trie["$"]
            return ""


        output = []
        words = sentence.split()
        for word in words:
            prefix = find_min_prefix(word, trie)
            if prefix == "":
                output.append(word)
            else:
                output.append(prefix)

        return " ".join(output)