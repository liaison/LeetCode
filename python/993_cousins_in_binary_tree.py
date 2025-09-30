# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def find_parent_depth(curr_node, parent_node, depth, value):
            if curr_node.val == value:
                return (parent_node, depth)

            for child in [curr_node.left, curr_node.right]:
                if child is not None:
                    search = find_parent_depth(child, curr_node, depth+1, value)
                    if search:
                        return search

            return None

        x_parent, x_depth = find_parent_depth(root, None, 0, x)
        y_parent, y_depth = find_parent_depth(root, None, 0, y)

        return (x_parent != y_parent and x_depth == y_depth)





