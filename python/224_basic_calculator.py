class SolutionTLE:
    """
        Aggregate all calculation at the end
        Time Limit Exceeded
    """
    def calculate(self, s: str) -> int:

        exp = (s + "+").replace(" ", "")
        end = len(exp)
        curr = 0

        def find_subexp_end(start):
            bracket_count = 0
            while True:
                if exp[start] == '(':
                    bracket_count += 1
                elif exp[start] == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        return start
                start += 1


        operand_stack = []
        num_list = []
        prev_sign = '+'

        while curr < end:

            if exp[curr] in ['+', '-']:
                # append the previous operand
                if len(num_list):
                    num = int("".join(num_list))
                    num_list = []
                    if prev_sign == '-':
                        num = -num
                    operand_stack.append(num)
                prev_sign = exp[curr]

            elif exp[curr] == '(':
                # calculate the sub-expression
                subexp_end = find_subexp_end(curr)
                sub_result = self.calculate(exp[(curr+1):subexp_end])
                if prev_sign == '-':
                    sub_result = - sub_result

                curr = subexp_end
                operand_stack.append(sub_result)

            else:
                # construct the operand
                num_list.append(exp[curr])

            curr += 1

        # aggregate all operands with '+' operator
        result = 0
        while operand_stack:
            result += operand_stack.pop()

        return result




class Solution:
    def calculate(self, s: str) -> int:
        stack, current = [], 0

        for c in '(' + s + ')':

            if c.isdigit():
                current = 10 * current + int(c)
            elif c == '(':
                # start a new expression
                stack += [0, '+']
                current = 0

            elif c != ' ':
                operator, previous = stack.pop(), stack.pop()
                current = previous + (current if operator == '+' else -current)

                # end of sub-expression
                if c == ')': continue

                # append the operand along with the next sign
                stack += [current, c]
                current = 0

        return current



class Solution:
    def calculate(self, s: str) -> int:
        operand_stack = []
        operator_stack = []
        cursor = 0
        number = 0
        end = len(s)

        def evaluate():
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            operator = operator_stack.pop()
            if operator == '+':
                return operand_1 + operand_2
            elif operator == '-':
                return operand_1 - operand_2

        priority_map = {'+': 0, '-': 0, '(': -1}

        while cursor < end:

            if s[cursor].isdigit():
                while cursor < end and s[cursor].isdigit():
                    number = number * 10 + int(s[cursor])
                    cursor += 1

                cursor -= 1
                operand_stack.append(number)
                number = 0

            elif s[cursor] in ['+', '-']:
                curr_operator = s[cursor]
                while operator_stack:
                    prev_operator = operator_stack[-1]
                    if priority_map[curr_operator] > priority_map[prev_operator]:
                        break
                    operand_stack.append(evaluate())

                # convert unary operator '-' to binary by appending a pseudo operand 0
                #  e.g.  -1 + 1 = 0 - 1 + 1
                if curr_operator == '-':
                    prev = cursor - 1
                    while prev >= 0 and s[prev] == ' ':
                        prev -= 1
                    if prev < 0 or s[prev] == '(':
                        operand_stack.append(0)

                operator_stack.append(curr_operator)

            elif s[cursor] == '(':
                operator_stack.append(s[cursor])

            elif s[cursor] == ')':
                while operator_stack[-1] != '(':
                    operand_stack.append(evaluate())

                operator_stack.pop()


            cursor += 1

        while operator_stack:
            operand_stack.append(evaluate())

        return operand_stack.pop()



