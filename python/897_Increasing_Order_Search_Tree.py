# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        value_list = []
        
        def dfs(node):
            nonlocal value_list    
            if node is None:
                return
            dfs(node.left)
            value_list.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        pseudo_head = TreeNode()
        prev_head = pseudo_head
        for value in value_list:
            prev_head.right = TreeNode(val=value)
            prev_head = prev_head.right
        
        return pseudo_head.right


class SolutionOnTheFly:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            node.left = None
            self.curr.right = node
            self.curr = node
            
            inorder(node.right)
            
        new_root = TreeNode()
        self.curr = new_root
        
        inorder(root)
        
        return new_root.right

