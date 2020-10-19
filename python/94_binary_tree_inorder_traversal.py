# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def inorderDFS(node, results):
            if not node:
                return
            
            inorderDFS(node.left, results)
            results.append(node.val)
            inorderDFS(node.right, results)
        
        
        results = []
        inorderDFS(root, results)
        
        return results
