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







