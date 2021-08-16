class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        to_remove = set()
        stack = []
        for index, letter in enumerate(s):
            if letter == "(":
                stack.append((index, letter))
            elif letter == ")":
                if stack:
                    stack.pop()
                else:
                    # invalid parenthese
                    to_remove.add(index)

        # list of unmatched (invalid) parentheses
        for index, letter in stack:
            to_remove.add(index)

        output = []
        for index, letter in enumerate(s):
            if index not in to_remove:
                output.append(letter)

        return "".join(output)