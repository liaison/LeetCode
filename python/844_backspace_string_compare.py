class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def simulate(string):
            """
                Simulate the input with backspace key (i.e. "#")
                return the remaining string
            """
            str_stack = []
            for letter in string:
                if letter == "#":
                    if str_stack:
                        str_stack.pop()
                else:
                    str_stack.append(letter)

            return "".join(str_stack)


        return simulate(s) == simulate(t)