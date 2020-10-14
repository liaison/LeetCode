# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        max_average = 0
        def averageAndCount(node):
            nonlocal max_average
            
            if not node.left and not node.right:
                max_average = max(node.val, max_average)
                return (node.val, 1)
            
            if node.left:
                left_avg, left_cnt = averageAndCount(node.left)
            else:
                left_avg = left_cnt = 0
            
            if node.right:
                right_avg, right_cnt = averageAndCount(node.right)
            else:
                right_avg = right_cnt = 0
            
            total_cnt = (left_cnt + right_cnt + 1)
            total_avg = (left_avg * left_cnt +  \
                         right_avg * right_cnt + node.val) / total_cnt
            
            max_average = max(max_average, left_avg, right_avg, total_avg)
            
            return (total_avg, total_cnt)
    
        if root:
            averageAndCount(root)
        
        return max_average
