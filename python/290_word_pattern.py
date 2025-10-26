class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        letter_to_word_map = {}
        word_to_letter_map = {}

        for index, letter in enumerate(pattern):

            word = words[index]

            if letter not in letter_to_word_map and word not in word_to_letter_map:
                letter_to_word_map[letter] = word
                word_to_letter_map[word] = letter

            elif letter_to_word_map.get(letter) != word or word_to_letter_map[word] != letter:
                return False

        return True

