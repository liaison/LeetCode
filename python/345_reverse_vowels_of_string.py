
class Solution:
    def reverseVowels(self, s: str) -> str:

        letter_list = []
        vowel_index_list = []

        VOWELS = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']

        for index, letter in enumerate(s):
            letter_list.append(letter)
            if letter in VOWELS:
                vowel_index_list.append(index)

        vowel_index = 0
        total_vowels = len(vowel_index_list)

        left, right = 0, len(vowel_index_list) - 1

        while left < right:
            left_index = vowel_index_list[left]
            right_index = vowel_index_list[right]
            letter_list[left_index], letter_list[right_index] \
                = letter_list[right_index], letter_list[left_index]

            left += 1
            right -= 1

        return "".join(letter_list)