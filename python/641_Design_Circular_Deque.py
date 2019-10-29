'''
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

- MyCircularDeque(k): Constructor, set the size of the deque to be k.
- insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
- insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
- deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
- deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
- getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
- getRear(): Gets the last item from Deque. If the deque is empty, return -1.
- isEmpty(): Checks whether Deque is empty or not. 
- isFull(): Checks whether Deque is full or not.

'''

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.count = 0
        self.queue = [0] * k
        self.head = 0


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.queue[self.head] = value
        self.count += 1
        return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        newTailIndex = (self.head + self.count) % self.capacity
        self.queue[newTailIndex] = value
        self.count += 1
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.count -= 1
        return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count == 0:
            return -1
        else:
            return self.queue[self.head]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count == 0:
            return -1
        else:
            tailIndex = (self.head + self.count - 1) % self.capacity
            return self.queue[tailIndex]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()