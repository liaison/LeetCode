# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        total_sum = 0

        def dfs(node, curr_num):
            nonlocal total_sum

            if node is None:
                return 0

            next_num = curr_num * 10 + node.val
            if node.left:
                dfs(node.left, next_num)

            if node.right:
                dfs(node.right, next_num)

            if node.left is None and node.right is None:
                # leaf node
                total_sum += next_num

        dfs(root, 0)
        return total_sum
