
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        def find_least_node(node):
            while node.left:
                node = node.left
            return node

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key == root.val
            # replace it with either of non-empty child node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # delete the current node by replacing it with the left most value on its right child
                left_most_node = find_least_node(root.right)
                root.val = left_most_node.val
                root.right = self.deleteNode(root.right, root.val)

        return root
