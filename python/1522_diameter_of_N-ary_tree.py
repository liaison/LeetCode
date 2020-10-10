"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_diameter = 0
        
        def max_depth(node, curr_depth):
            nonlocal max_diameter
            
            if len(node.children) == 0:
                return curr_depth
            
            depths= []
            for child in node.children:
                depths.append(max_depth(child, curr_depth+1))
             
            depths.sort(reverse = True)
            
            # calculate the distance between two farthest children
            max_diameter = max(max_diameter, sum(depths[0:2]) - 2 * curr_depth)
            
            return depths[0]
        
        max_depth(root, 0)
        
        return max_diameter
