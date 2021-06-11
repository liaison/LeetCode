
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        def count_letter(word):
            letter_cnt = defaultdict(int)
            for letter in word:
                letter_cnt[letter] += 1
            return letter_cnt


        ransom_dict = count_letter(ransomNote)
        magazine_dict = count_letter(magazine)

        for letter, cnt in ransom_dict.items():
            if letter not in magazine_dict:
                return False
            if cnt > magazine_dict[letter]:
                return False

        return True

