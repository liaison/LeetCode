# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        max_zigzag = -1

        def dfs(node):
            nonlocal max_zigzag

            if node is None:
                return (-1, -1)

            left_left, left_right = dfs(node.left)
            right_left, right_right = dfs(node.right)

            max_zigzag = max(max_zigzag, left_left, left_right, right_left, right_right)

            return (left_right + 1, right_left + 1)

        left, right = dfs(root)
        max_zigzag = max(max_zigzag, left, right)

        return max_zigzag
