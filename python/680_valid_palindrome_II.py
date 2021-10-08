class Solution:
    def validPalindrome(self, s: str) -> bool:

        @functools.lru_cache(maxsize=None)
        def is_palindrome(left, right, is_deleted):
            if left >= right:
                return True

            if s[left] == s[right]:
                return is_palindrome(left+1, right-1, is_deleted)
            else:
                if is_deleted:
                    return False

                if is_palindrome(left+1, right, True):
                    return True
                else:
                    return is_palindrome(left, right-1, True)

        return is_palindrome(0, len(s)-1, False)

