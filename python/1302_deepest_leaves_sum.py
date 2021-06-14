
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def get_leaves(node, depth, leaves_list):
            if node is None:
                return

            if node.left is not None:
                get_leaves(node.left, depth+1, leaves_list)
            if node.right is not None:
                get_leaves(node.right, depth+1, leaves_list)
            else:
                leaves_list.append((depth, node.val))

        leaves_list = []
        get_leaves(root, 0, leaves_list)

        max_depth, _ = max(leaves_list, key=lambda x:x[0])
        return sum([val for depth, val in leaves_list if depth == max_depth])
