# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def cumulative_sum(node, cum_sum):
            """
                Idea: update each node with the cumulative sum in the order of in-order traversal.

                In-order traversal,
                    first right, then middle, then left
                    at each node, we update the value with the cumulative sum sofar.
            """
            if not node:
                return cum_sum

            right_sum = cumulative_sum(node.right, cum_sum)
            node.val = node.val + right_sum

            return cumulative_sum(node.left, node.val)

        cumulative_sum(root, 0)

        return root
