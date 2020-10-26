# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def dfs(node):
            if node is None:
                return True
            
            remove_left = dfs(node.left)
            if remove_left:
                node.left = None
            
            remove_right = dfs(node.right)
            if remove_right:
                node.right = None
            
            if node.val == target:
                return (remove_left and remove_right)
            
            return False
        
        pseudo_head = TreeNode(val=0, left=root)
        dfs(pseudo_head)
        
        return pseudo_head.left
