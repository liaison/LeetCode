class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = { ")": "(", "}": "{" , "]": "["}

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            else:
                if stack and stack.pop() == bracket_map[char]:
                    continue
                else:
                    return False

        return len(stack) == 0
