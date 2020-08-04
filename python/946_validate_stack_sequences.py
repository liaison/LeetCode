class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        if len(pushed) == 0:
            return len(popped) == 0
        
        stack = list()
        push_curr, pop_curr = 1, 0
        stack.append(pushed[0])
        
        while pop_curr < len(popped):
            
            if len(stack) > 0 and popped[pop_curr] == stack[-1]:
                stack.pop()
                pop_curr += 1
            elif push_curr < len(pushed):
                stack.append(pushed[push_curr])
                push_curr += 1
            else:
                return False
        
        return pop_curr == len(popped)