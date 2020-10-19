# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        min_diff = float('inf')
        
        def dfs(node):
            nonlocal min_diff
            if not node:
                return (-1, -1)
            
            l_min_val, l_max_val = dfs(node.left)
            r_min_val, r_max_val = dfs(node.right)
        
            if l_max_val != -1:
                min_diff = min(min_diff, abs(l_max_val - node.val))
            else:
                l_min_val = node.val
                
            if r_min_val != -1:
                min_diff = min(min_diff, abs(r_min_val - node.val))
            else:
                r_max_val = node.val
            
            return min(l_min_val, node.val), max(node.val, r_max_val)
        
        dfs(root)
        
        return min_diff
