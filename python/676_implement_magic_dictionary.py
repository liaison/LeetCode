
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_dict = {}


    def buildDict(self, dictionary: List[str]) -> None:

        def index_word(word):
            word_group = len(word)
            if word_group not in self.trie_dict:
                self.trie_dict[word_group] = {}

            curr_node = self.trie_dict[word_group]

            for letter in word:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]

        for word in dictionary:
            index_word(word)


    def search(self, searchWord: str) -> bool:

        def dfs(node, index, unmatched_once):
            if index == len(searchWord):
                return unmatched_once

            letter = searchWord[index]
            # Backtracking on the match of letter
            #    try both matched and unmatched cases
            for next_letter in node.keys():
                if letter != next_letter:
                    if unmatched_once:
                        continue
                    if dfs(node[next_letter], index+1, True):
                        return True
                else:
                    if dfs(node[next_letter], index+1, unmatched_once):
                        return True

            return False

        word_group = len(searchWord)
        if word_group not in self.trie_dict:
            return False

        start_node = self.trie_dict[word_group]
        return dfs(start_node, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)