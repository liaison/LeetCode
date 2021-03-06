class Solution:
    def calculate(self, s: str) -> int:
        """ https://en.wikipedia.org/wiki/Shunting-yard_algorithm
        """
        def calculate():
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            operator = operator_stack.pop()
            
            if operator == '*':
                result = operand_1 * operand_2
            elif operator == "/":
                result = int(operand_1 / operand_2)
            elif operator == "+":
                result = operand_1 + operand_2
            else:
                result = operand_1 - operand_2
        
            operand_stack.append(result)
                
        
        s = s.replace(" ", '')
        
        operand_stack = []
        operator_stack = []
        
        operand = []
        priority = {"*": 2, "/": 2, "+": 1, "-": 1}
        
        for letter in s:
            if not letter.isnumeric():
                
                operand_str = "".join(operand)
                operand = []
                operand_stack.append(int(operand_str))
                
                if len(operator_stack) == 0:
                    operator_stack.append(letter)
                    continue
                
                while operator_stack and priority[operator_stack[-1]] >= priority[letter]:
                    calculate()
                
                operator_stack.append(letter)
            else:
                operand.append(letter)
        
        # add the last operand
        operand_stack.append(int("".join(operand)))
        
        # calculate the rest of the expressions
        while operator_stack:
            calculate()
            
        return operand_stack[-1]


class SolutionPseudoTail:
    def calculate(self, s: str) -> int:
        
        def calculate():
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            operator = operator_stack.pop()
            
            if operator == '*':
                result = operand_1 * operand_2
            elif operator == "/":
                result = int(operand_1 / operand_2)
            elif operator == "+":
                result = operand_1 + operand_2
            else:
                result = operand_1 - operand_2
        
            operand_stack.append(result)
                
        
        s = s.replace(" ", '')
        
        operand_stack = []
        operator_stack = []
        
        operand = []
        priority = {"*": 2, "/": 2, "+": 1, "-": 1}

        # add a pseudo tail to evaluate all expressions at the end.
        for letter in s + "+":
            if not letter.isnumeric():
                
                operand_str = "".join(operand)
                operand = []
                operand_stack.append(int(operand_str))
                
                if len(operator_stack) == 0:
                    operator_stack.append(letter)
                    continue
                
                while operator_stack and priority[operator_stack[-1]] >= priority[letter]:
                    calculate()
                
                operator_stack.append(letter)
            else:
                operand.append(letter)

        return operand_stack[-1]


class SolutionOperandStack:
    def calculate(self, s: str) -> int:
        
        component_stack = []
        operand = 0
        # a pseudo head to add the first operand
        pre_operator = "+"
        
        # add a pseudo tail to evaluate all expressions at the end.
        for letter in s + "+":
            if letter == " ":
                pass
            elif not letter.isnumeric():
                # encounter a new operator
                
                if pre_operator == "+":
                    component_stack.append(operand)
                elif pre_operator == "-":
                    component_stack.append(-operand)
                elif pre_operator == "*":
                    pre_operand = component_stack.pop()
                    component_stack.append(pre_operand * operand)
                elif pre_operator == "/":
                    pre_operand = component_stack.pop()
                    component_stack.append(int(pre_operand / operand))
                
                # prepare for the next expression
                operand = 0
                pre_operator = letter
            else:
                operand = operand * 10 + int(letter)

        return sum(component_stack)


