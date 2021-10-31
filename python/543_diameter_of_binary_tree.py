# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        max_diameter = 0

        def max_depth(node, curr_depth):
            nonlocal max_diameter

            if node is None:
                return curr_depth - 1

            # at each node, calculate the maximal distance between two children nodes
            left_depth = max_depth(node.left, curr_depth+1)
            right_depth = max_depth(node.right, curr_depth+1)
            max_diameter = max(max_diameter, left_depth + right_depth - 2 * curr_depth)

            return max(left_depth, right_depth)

        max_depth(root, 0)

        return max_diameter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWithHeight:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        max_diameter = 0

        def height(node):
            """
                return: height of the node
                    max(height(node.left), height(node.right)) + 1
            """
            nonlocal max_diameter

            if not node:
                return 0

            max_left = height(node.left)
            max_right = height(node.right)
            max_diameter = max(max_diameter, max_left + max_right)

            return max(max_left, max_right) + 1

        height(root)

        return max_diameter