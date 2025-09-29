"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        max_depth = 0

        def dfs(node, curr_depth):
            nonlocal max_depth

            if node is None:
                return

            if len(node.children) == 0:
                max_depth = max(max_depth, curr_depth)
            else:
                for child in node.children:
                    dfs(child, curr_depth+1)

        dfs(root, 1)

        return max_depth


    def maxDepth_rec(self, root: 'Node') -> int:

        if not root:
            return 0

        max_depth = 1
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth_rec(child) + 1)

        return max_depth


    def maxDepth_py(self, root: 'Node') -> int:

        if not root:
            return 0

        # avoid max([]) error
        if len(root.children) == 0:
            return 1

        return max([self.maxDepth_py(child) for child in root.children]) + 1
