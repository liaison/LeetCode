# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        
        def distance_to_leave(node):
            nonlocal results
            
            if node is None:
                return 0
            
            distance = 1 + max(distance_to_leave(node.left),
                               distance_to_leave(node.right))
            
            # update the resulting array
            if distance > len(results):
                results.append([node.val])
            else:
                results[distance-1].append(node.val)
        
            # return the maximum distance to any of the leaves
            return distance
        
        distance_to_leave(root)
        
        return results
