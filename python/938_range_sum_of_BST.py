# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        value_sum = 0
        def dfs(node):
            nonlocal value_sum
            if not node:
                return
            if L <= node.val <= R:
                value_sum += node.val
            
            if node.val >= L:
                dfs(node.left)
            if node.val <= R:
                dfs(node.right)

        dfs(root)
        
        return value_sum