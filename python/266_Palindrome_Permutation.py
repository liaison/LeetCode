class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_set = set()

        for char in s:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)
        return len(char_set) <= 1
