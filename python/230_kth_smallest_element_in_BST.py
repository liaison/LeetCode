# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ordered_list = []

        def inorder_traverse(node):
            nonlocal ordered_list

            if not node:
                return

            if len(ordered_list) >= k:
                return

            inorder_traverse(node.left)
            ordered_list.append(node.val)
            inorder_traverse(node.right)

        inorder_traverse(root)

        return ordered_list[k-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionConstantSpace:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        index_num = (-1, 0)

        def inorder_traverse(node):
            nonlocal index_num

            if not node:
                return

            # Early interrupt for the traversal
            index, num = index_num
            if index == k-1:
                return

            inorder_traverse(node.left)

            index, num = index_num
            if index < k-1:
                index_num = index+1, node.val

            inorder_traverse(node.right)

        inorder_traverse(root)

        return index_num[1]


