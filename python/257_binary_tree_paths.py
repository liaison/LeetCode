# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        output = []
        
        def backtrack(node, path):
            
            if node.left is None and node.right is None:
                output.append("->".join(path))
                return
            
            for child in [node.left, node.right]:
                if child is None:
                    continue
                path.append(str(child.val))
                backtrack(child, path)
                path.pop()
        
        if root is not None:
            path = [str(root.val)]
            backtrack(root, path)
        
        return output
