class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        trie = {}

        def update_trie(word, trie_node):
            for letter in word:
                if letter not in trie_node:
                    trie_node[letter] = {}
                trie_node = trie_node[letter]

            # trie_node["$"] keeps the number of words that reaches this node
            # Note: the words could be duplicated in the list
            if "$" not in trie_node:
                trie_node["$"] = 1
            else:
                trie_node["$"] += 1

        for word in words:
            update_trie(word, trie)


        def count_words(contain_first, first_letter, letter_set, trie_node, matched_words):
            """
                Run DFS to find all the matched nodes
            """
            for letter in trie_node.keys():
                if letter == "$" and contain_first:
                    matched_words.append(trie_node['$'])
                else:
                    if letter in letter_set:
                        is_first = (letter == first_letter)
                        count_words(contain_first or is_first, first_letter, letter_set, trie_node[letter], matched_words)

        answer = []
        for puzzle in puzzles:
            letter_set = set(puzzle)
            matched_words = []
            contain_first = False

            count_words(contain_first, puzzle[0], letter_set, trie, matched_words)
            answer.append(sum(matched_words))

        return answer


