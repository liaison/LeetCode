# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        count = 0

        def dfs_backtrack(node, prefix_sums):
            nonlocal count
            
            if node is None:
                return
            
            prefix_sums.append(prefix_sums[-1] + node.val)
            
            for i in range(len(prefix_sums)-1):
                if prefix_sums[-1] - prefix_sums[i] == sum:
                    count += 1                   
            dfs_backtrack(node.left, prefix_sums)
            dfs_backtrack(node.right, prefix_sums)
            
            # backtracking operation
            prefix_sums.pop()
            
        
        dfs_backtrack(root, [0])
        
        return count
