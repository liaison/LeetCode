# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest_node = root
        # traverse the BST in the order of binary search
        #   check every node that we traverse.
        while root:
            closest_node = min(root, closest_node, key = lambda x: abs(target - x.val))
            
            # next iteration
            root = root.left if target < root.val else root.right
        
        return closest_node.val