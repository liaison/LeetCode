
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for letter in s:
            if not stack:
                stack.append((letter, 1))
            else:
                prev_letter, count = stack[-1]
                if letter == prev_letter:
                    if count == k - 1:
                        for _ in range(k-1):
                            stack.pop()
                    else:
                        stack.append((letter, count+1))
                else:
                    stack.append((letter, 1))

        return "".join([l for (l, c) in stack])
