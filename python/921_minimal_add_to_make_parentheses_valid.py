class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        missing_count = 0
        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            else: # ")"
                if len(stack) == 0:
                    missing_count += 1
                else:
                    stack.pop()

        return missing_count + len(stack)
