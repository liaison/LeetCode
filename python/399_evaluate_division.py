class Node:
    def __init__(self, tag):
        self.tag = tag
        self.divisors = {}
        self.visited = False
    
    def add_divisor(self, divisor, value):
        self.divisors[divisor.tag] = (divisor, value)

    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        variables = {}
        
        for equation, value in zip(equations, values):
            divident, divisor = equation[0], equation[1]
            
            if divident not in variables:
                variables[divident] = Node(divident)
            var_divident = variables[divident]
            
            if divisor not in variables:
                variables[divisor] = Node(divisor)
            var_divisor = variables[divisor]
            
            var_divident.add_divisor(var_divisor, value)
            var_divisor.add_divisor(var_divident, 1 / value)
        
        
        def backtrack_evaluate(curr_node, target_tag, acc_product):
            curr_node.visited = True
            ret = - 1.0
            
            if target_tag in curr_node.divisors:
                ret = acc_product * (curr_node.divisors[target_tag][1])
            else:
                for key, value_tuple in curr_node.divisors.items():
                    divisor, value = value_tuple
                    if divisor.visited:
                        continue
                    
                    ret = backtrack_evaluate(divisor, target_tag, value * acc_product)
                    if ret != -1.0:
                        break
            
            curr_node.visited = False
            return ret
      
        
        results = []
        for query in queries:
            if query[0] not in variables:
                ret = -1.0
            elif query[0] == query[1]:
                ret = 1.0
            else:
                start_node = variables[query[0]]
                ret = backtrack_evaluate(start_node, query[1], 1)
            results.append(ret)
        
        
        return results
