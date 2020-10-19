class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            
            to_add = True
            
            while stack:
                tail = stack[-1]
                if (tail * asteroid > 0) or (tail < 0 and asteroid > 0):
                    stack.append(asteroid)
                    to_add = False
                    break
                else:
                    # collision
                    if abs(tail) > abs(asteroid):
                        # current asteroid is destroyed
                        to_add = False
                        break
                    elif abs(tail) == abs(asteroid):
                        # both asteroid is destroyed
                        stack.pop()
                        to_add = False
                        break
                    else:
                        # previous asteroid is destroyed
                        stack.pop()
            if to_add:
                # we still need to add the current asteroid into the stack
                stack.append(asteroid)
                
        return stack