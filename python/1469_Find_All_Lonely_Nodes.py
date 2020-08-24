# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely_nodes = []
        
        def dfs(node, is_lonely):
            if node is None:
                return
            
            if is_lonely:
                lonely_nodes.append(node.val)
                
            if (node.left is None) ^ (node.right is None):
                is_lonely = True
            else:
                is_lonely = False
            
            dfs(node.left, is_lonely)
            dfs(node.right, is_lonely)
    
        dfs(root, False)
        
        return lonely_nodes