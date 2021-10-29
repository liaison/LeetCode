class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
            else:
                top = stack[-1]
                if top == letter:
                    stack.pop()
                else:
                    stack.append(letter)

        return "".join(stack)
