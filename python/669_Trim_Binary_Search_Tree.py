# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        if root is None:
            return root
        
        left_child = self.trimBST(root.left, low, high)
        right_child = self.trimBST(root.right, low, high)
        
        if root.val < low or root.val > high:
            # trim the current node
            root = left_child or right_child
        else:
            root.left = left_child
            root.right = right_child
        
        return root