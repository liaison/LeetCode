class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        start = 0
        primitives = []
        # retrieve all the primitives
        for index, letter in enumerate(s):
            if letter == "(":
                stack.append(letter)
            else:
                stack.pop()
                if len(stack) == 0:
                    primitives.append(s[start:index+1])
                    start = index + 1

        # strip the outermost parentheses
        stripped = []
        for primitive in primitives:
            stripped.append(primitive[1:-1])

        return "".join(stripped)

