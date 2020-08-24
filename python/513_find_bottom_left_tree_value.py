# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        leaves_list = []
        
        def dfs(node, row, col):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                leaves_list.append((-row, col, node.val))
            else:
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        
        # order the leaves nodes by its (row, col) index
        leaves_list.sort()
        
        return leaves_list[0][2]
