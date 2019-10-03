"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

class MovingAverage:
    """
        Design a circular queue with array,
            with minimal calculation and space consumption 
    """
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        
        """
        self.size = size
        self.queue = [0] * self.size
        self.curr = 0
        self.sum = 0 
        self.count = 0
    
    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.curr + self.size + 1) % self.size
        self.sum = self.sum - self.queue[tail] + val
        # move on to the next head
        self.curr = (self.curr + 1) % self.size
        self.queue[self.curr] = val

        return self.sum / (self.size if self.count > self.size else self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)