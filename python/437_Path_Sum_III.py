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

    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionHashTable:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        count = 0
        prefix_sums_count = defaultdict(int)
        
        def dfs_backtrack(node, acc_sum):
            nonlocal count
            
            if node is None:
                return
            
            acc_sum += node.val
            if acc_sum == sum:
                count += 1
            
            count += prefix_sums_count[acc_sum - sum]
            
            # mark the current prefix sum
            prefix_sums_count[acc_sum] += 1
            
            dfs_backtrack(node.left, acc_sum)
            dfs_backtrack(node.right, acc_sum)
            
            # backtracking operation
            prefix_sums_count[acc_sum] -= 1
            
        
        dfs_backtrack(root, 0)
        
        return count