from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def contains(counter_one, counter_other):
            for letter in counter_other:
                if letter not in counter_one:
                    return False
                elif counter_one[letter] < counter_other[letter]:
                    return False

            return True

        word_sum = 0
        char_counter = Counter(chars)
        for word in words:
            word_counter = Counter(word)
            if contains(char_counter, word_counter):
                word_sum += len(word)

        return word_sum






