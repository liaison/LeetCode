# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def dfs(node, value):
            next_node = None
            if value < node.val:
                if node.left is None:
                    # insert as the new left child
                    node.left = TreeNode(value)
                    return
                else:
                    next_node = node.left
            else: # value > node.val
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                else:
                    next_node = node.right
            # continue the search
            dfs(next_node, value)
        
        if root is None:
            return TreeNode(val)
        else:
            dfs(root, val)
            return root
