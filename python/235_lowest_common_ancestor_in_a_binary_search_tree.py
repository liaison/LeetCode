# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        earliest_node = None
        def count_appearance(node):
            nonlocal earliest_node

            if not node:
                return 0

            if earliest_node:
                # terminate the recursion process when we
                #  find the common ancestor
                return 0

            left = count_appearance(node.left)
            right = count_appearance(node.right)

            mid = 1 if node.val in [p.val, q.val] else 0

            count = left + right + mid
            if count >= 2 and not earliest_node:
                earliest_node = node

            return count

        count_appearance(root)

        return earliest_node

