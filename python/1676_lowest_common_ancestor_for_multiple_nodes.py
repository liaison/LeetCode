
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        value_subset = set([node.val for node in nodes])

        result = None
        def get_descendants(parent):
            nonlocal result

            if not parent:
                return set()

            left_nodes = get_descendants(parent.left)
            if result:
                return set()
            right_nodes = get_descendants(parent.right)

            all_nodes = {parent.val} | left_nodes | right_nodes

            if value_subset.issubset(all_nodes) and not result:
                result = parent

            return all_nodes

        get_descendants(root)
        return result
