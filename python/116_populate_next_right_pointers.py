
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = deque([root, None])
        while len(queue) > 1:

            tail = queue.pop()
            next_queue = deque([None])

            for _ in range(len(queue)):
                curr = queue.pop()
                curr.next = tail

                if curr.right:
                    next_queue.appendleft(curr.right)
                    next_queue.appendleft(curr.left)
                # move the tail pointer
                tail = curr

            queue = next_queue

        return root




