"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return root

        node_copy = Node(root.val)
        for child in root.children:
            node_copy.children.append(self.cloneTree(child))

        return node_copy
