import math

class Solution:
    def calculate(self, s: str) -> int:

        cursor = 0
        end = len(s)

        priority_map = {"+": 0, "-": 0, '*': 1, '/': 1}

        def evaluate(operand_1, operand_2, operator):
            if operator == '+':
                return operand_1 + operand_2
            elif operator == '-':
                return operand_1 - operand_2
            elif operator == '*':
                return operand_1 * operand_2
            else:
                return math.trunc(operand_1 / operand_2)


        def find_subexp_end(start):
            bracket_count = 0
            while True:
                if s[start] == '(':
                    bracket_count += 1
                elif s[start] == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        return start
                start += 1


        operand_stack = []
        operator_stack = []

        substr_list = []

        # Evaluate the expression on-the-go, according to the priority.
        while cursor < end:
            if s[cursor] in ['+', '-', '*', '/']:

                curr_operator = s[cursor]

                if len(substr_list):
                    operand = int("".join(substr_list))
                    substr_list = []
                    operand_stack.append(operand)

                while operator_stack:
                    pre_operator = operator_stack[-1]
                    if priority_map[curr_operator] > priority_map[pre_operator]:
                        break
                    # evaluate the remaining sub expressions
                    operand_2 = operand_stack.pop()
                    operand_1 = operand_stack.pop()

                    result = evaluate(operand_1, operand_2, operator_stack.pop())
                    operand_stack.append(result)

                operator_stack.append(curr_operator)


            elif s[cursor] == '(':

                next_cursor = find_subexp_end(cursor)

                sub_exp = s[(cursor+1):next_cursor]
                operand_stack.append(self.calculate(sub_exp))

                # end of the sub expression
                cursor = next_cursor

            else: # numbers
                substr_list.append(s[cursor])


            cursor += 1

        # Evaluate the remaining expressions
        if len(substr_list):
            operand_stack.append(int("".join(substr_list)))

        while operator_stack:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            result = evaluate(operand_1, operand_2, operator_stack.pop())
            operand_stack.append(result)


        return operand_stack.pop()



class SolutionPseudoEnd:
    def calculate(self, s: str) -> int:

        cursor = 0
        # '!': pseudo operator to mark the end of string
        #   in order to make the code more concise
        s = s + '!'

        end = len(s)

        priority_map = {"+": 0, "-": 0, '*': 1, '/': 1, '!': -1}

        def evaluate(operand_1, operand_2, operator):
            if operator == '+':
                return operand_1 + operand_2
            elif operator == '-':
                return operand_1 - operand_2
            elif operator == '*':
                return operand_1 * operand_2
            else:
                return math.trunc(operand_1 / operand_2)


        def find_subexp_end(start):
            bracket_count = 0
            while True:
                if s[start] == '(':
                    bracket_count += 1
                elif s[start] == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        return start

                start += 1


        operand_stack = []
        operator_stack = []

        substr_list = []

        while cursor < end:
            if s[cursor] in ['+', '-', '*', '/', '!']:

                curr_operator = s[cursor]

                if len(substr_list):
                    operand = int("".join(substr_list))
                    substr_list = []
                    operand_stack.append(operand)

                while operator_stack:
                    pre_operator = operator_stack[-1]
                    if priority_map[curr_operator] > priority_map[pre_operator]:
                        break
                    # evaluate the remaining sub expressions
                    operand_2 = operand_stack.pop()
                    operand_1 = operand_stack.pop()

                    result = evaluate(operand_1, operand_2, operator_stack.pop())
                    operand_stack.append(result)

                operator_stack.append(curr_operator)


            elif s[cursor] == '(':
                next_cursor = find_subexp_end(cursor)
                sub_exp = s[(cursor+1):next_cursor]
                operand_stack.append(self.calculate(sub_exp))

                # end of the sub expression
                cursor = next_cursor

            else: # numbers
                substr_list.append(s[cursor])


            cursor += 1

        return operand_stack.pop()




class SolutionIteration:
    def calculate(self, s: str) -> int:

        precedence = {"+": 0, "-": 0, '*': 1, '/': 1, '(': -1}

        operand_stack = []
        operator_stack = []

        def evaluate():
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            operator = operator_stack.pop()

            if operator == '+':
                return operand_1 + operand_2
            elif operator == '-':
                return operand_1 - operand_2
            elif operator == '*':
                return operand_1 * operand_2
            else:
                return math.trunc(operand_1 / operand_2)

        number = 0
        cursor = 0
        end = len(s)

        while cursor < end:
            if s[cursor].isdigit():
                # scan through all digits in an operand
                number = int(s[cursor])
                while cursor+1 < end and s[cursor+1].isdigit():
                    number = number * 10 + int(s[cursor+1])
                    cursor += 1

                operand_stack.append(number)
                number = 0

            elif s[cursor] in ['+', '-', '*', '/']:

                curr_operator = s[cursor]

                while operator_stack:
                    prev_operator = operator_stack[-1]
                    if precedence[curr_operator] > precedence[prev_operator]:
                        break
                    # evaluate the preceding expressions
                    operand_stack.append(evaluate())

                operator_stack.append(curr_operator)

            elif s[cursor] == '(':

                operator_stack.append("(")

            elif s[cursor] == ')':
                # evaluate the sub-expression with bracket ()
                while operator_stack[-1] != "(":
                    operand_stack.append(evaluate())
                # pop the artifical '(' operator
                operator_stack.pop()


            cursor += 1

        # evaluate the remaining expressions
        while operator_stack:
            operand_stack.append(evaluate())


        return operand_stack.pop()























