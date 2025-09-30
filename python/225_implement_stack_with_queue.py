class MyStack:

    def __init__(self):
        self.queue = deque()
        self.size = 0
        self.top_element = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_element = x
        self.size += 1

    def pop(self) -> int:
        if self.size < 1:
            return -1

        temp_queue = deque()
        count = 0
        new_top_element = None
        while count < self.size - 1:
            element = self.queue.popleft()
            temp_queue.append(element)

            if count == self.size - 2:
                new_top_element = element
            count += 1

        top = self.queue.popleft()
        self.queue = temp_queue
        self.size -= 1
        self.top_element =  new_top_element
        return top


    def top(self) -> int:
        if self.size < 1:
            return -1

        return self.top_element


    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()