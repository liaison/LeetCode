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


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class SolutionDFS:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return root

        new_root = Node(root.val)

        # DFS/BFS
        stack = [(root, new_root)]
        while stack:
            old_node, new_node = stack.pop()
            for child_node in old_node.children:
                new_child_node = Node(child_node.val)
                new_node.children.append(new_child_node)
                # 'recursively' make deep copy for each child node
                stack.append((child_node, new_child_node))

        return new_root
