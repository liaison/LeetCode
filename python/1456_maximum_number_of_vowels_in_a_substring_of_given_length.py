
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        VOWELS = ['a', 'e', 'i', 'o', 'u']
        vowel_cnt = 0
        for letter in s[0:k]:
            if letter in VOWELS:
                vowel_cnt += 1

        # starting number of vowels in a sliding window
        max_vowel_cnt = vowel_cnt

        for index in range(k, len(s)):
            out_of_index = index - k
            # two pointers that defines the boundary of the sliding window
            if s[index] in VOWELS:
                vowel_cnt += 1

            if s[out_of_index] in VOWELS:
                vowel_cnt -= 1

            max_vowel_cnt = max(max_vowel_cnt, vowel_cnt)

        return max_vowel_cnt