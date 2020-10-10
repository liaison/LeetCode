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
            
            depths = []
            for child in node.children:
                depths.append(max_depth(child, curr_depth+1))
             
            depths.sort(reverse = True)
            
            # calculate the distance between two farthest children
            max_diameter = max(max_diameter, sum(depths[0:2]) - 2 * curr_depth)
            
            return depths[0]
        
        max_depth(root, 0)
        
        return max_diameter


class SolutionNoSorting:
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
            
            max_depth_1, max_depth_2 = 0, curr_depth
            for child in node.children:
                depth = max_depth(child, curr_depth+1)
                if depth > max_depth_1:
                    max_depth_1, max_depth_2 = depth, max_depth_1
                elif depth > max_depth_2:
                    max_depth_2 = depth
            
            # calculate the distance between two farthest children
            max_diameter = max(max_diameter,
                max_depth_1 + max_depth_2 - 2 * curr_depth)
            
            return max_depth_1
        
        max_depth(root, 0)
        
        return max_diameter

                
