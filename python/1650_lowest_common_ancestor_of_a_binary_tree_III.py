

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
            Bidirectional BFS search to find the earliest intersection,
            It is generic that it can be applied to the graph data structure as well.
        """
        seen = set()
        queue = deque([q, p])

        while queue:
            curr_node = queue.popleft()
            if curr_node.val in seen:
                return curr_node

            seen.add(curr_node.val)

            if curr_node.parent:
                queue.append(curr_node.parent)

