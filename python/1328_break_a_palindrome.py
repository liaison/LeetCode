class Solution:

    def breakPalindrome(self, palindrome: str) -> str:
        """
            Greedy strategy to build the first non-palindrome string.
            3 rules in total:
                - the string is of one letter
                - find the first non-a letter in the first half of the palindrome string,
                    and replace it with the letter 'a'.
                - otherwise replace the last letter with 'a'.
        """
        if len(palindrome) == 1:
            return ""

        mid = len(palindrome) // 2

        for index in range(mid):
            if palindrome[index] != 'a':
                return palindrome[0:index] + "a" + palindrome[index+1:]

        return palindrome[:-1] + "b"
