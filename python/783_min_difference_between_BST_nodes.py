# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        min_diff = float('inf')
        
        def dfs(node):
            nonlocal min_diff
            
            if not node:
                return (None, None)
            
            l_min_val, l_max_val = dfs(node.left)
            r_min_val, r_max_val = dfs(node.right)
            
            if l_max_val:
                min_diff = min(min_diff, abs(node.val - l_max_val))
            else:
                l_min_val = node.val
            
            if r_min_val:
                min_diff = min(min_diff, abs(node.val - r_min_val))
            else:
                r_max_val = node.val
            
            return min(l_min_val, node.val), max(r_max_val, node.val)
        
        dfs(root)
        
        return min_diff
