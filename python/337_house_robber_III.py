# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(node, can_rob, acc_sum):    
            if not node:
                return acc_sum
            
            max_sum = acc_sum
            
            if can_rob:
                # rob the current node
                left_sum = dfs(node.left, False, 0)
                right_sum = dfs(node.right, False, 0)
                max_sum += node.val + left_sum + right_sum
            
            # either cannot or choose not to rob the current node
            left_sum = dfs(node.left, True, 0)
            right_sum = dfs(node.right, True, 0)
            max_sum = max(max_sum, left_sum + right_sum)
            
            return max_sum
        
        first_try = dfs(root, True, 0)
        second_try = dfs(root, False, 0)
        
        return max(first_try, second_try)

