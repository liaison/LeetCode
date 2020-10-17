# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        max_bst_size = 0
        
        def dfs(node):
            nonlocal max_bst_size
            
            if not node:
                # is_bst, num_nodes, min_value, max_value
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_num_nodes, left_min_value, left_max_value = dfs(node.left)
            right_is_bst, right_num_nodes, right_min_value, right_max_value = dfs(node.right)
                
            if left_is_bst and right_is_bst:
                
                # the conditions should be this, according to the definition of BST
                #if left_max_value <= node.val <= right_min_value:
                
                if left_max_value < node.val < right_min_value:
                    bst_size = 1 + left_num_nodes + right_num_nodes
                    
                    max_bst_size = max(max_bst_size, bst_size)
                    
                    min_value = min(node.val, left_min_value)
                    max_value = max(node.val, right_max_value)
                    
                    return (True, bst_size, min_value, max_value)
            
            return (False, 0, float('inf'), float('-inf'))
        
        dfs(root)
        
        return max_bst_size