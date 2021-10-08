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


class SolutionDFS:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        queue = [(left, right, 0)]
        while queue:
            left, right, delete_count = queue.pop()
            if left >= right:
                return True

            if s[left] == s[right]:
                queue.append((left+1, right-1, delete_count))
            else:
                if delete_count < 1:
                    queue.append((left+1, right, delete_count+1))
                    queue.append((left, right-1, delete_count+1))

        return left >= right


class SolutionGreedy:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while s[left] == s[right] and left < right:
            left += 1
            right -= 1

        delete_left = s[left+1:right+1]
        delete_right = s[left:right]

        return delete_left == delete_left[::-1] or delete_right == delete_right[::-1]

