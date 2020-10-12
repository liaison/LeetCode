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
