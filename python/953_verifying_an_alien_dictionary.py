class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # handle the edge case, as well as a cheap optimization
        if len(words) <= 1:
            return True

        letter_order = {}
        for rank, letter in enumerate(order):
            letter_order[letter] = rank

        def is_less_than(word1, word2):
            bound = min(len(word1), len(word2))
            index = 0
            while index < bound:
                if letter_order[word1[index]] < letter_order[word2[index]]:
                    return True
                elif letter_order[word1[index]] > letter_order[word2[index]]:
                    return False
                index += 1

            return True if len(word1) <= len(word2) else False


        prev_word = words[0]
        for next_word in words[1:]:
            if not is_less_than(prev_word, next_word):
                return False
            prev_word = next_word


        return True


