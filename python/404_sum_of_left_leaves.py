# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        leaf_sum = 0
        def dfs(node, is_left=None):
            nonlocal leaf_sum
            if node is None:
                return
            
            if node.left is None and node.right is None and is_left:
                leaf_sum += node.val
            else:
                dfs(node.left, True)
                dfs(node.right, False)
        
        dfs(root)
        return leaf_sum
