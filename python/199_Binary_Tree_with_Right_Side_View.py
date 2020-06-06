# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        results = []
        
        def DFS(node, depth):
            if node:
                if depth == len(results):
                    results.append(node.val)
                # preorder with the priority on the right child
                DFS(node.right, depth+1)
                DFS(node.left, depth+1)
        
        DFS(root , 0)
        return results
