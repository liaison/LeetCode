# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        # node_str -> node
        node_str_set = set()
        duplicated_strs = set()
        duplicated_nodes = list()


        def node2str(node):
            """
                this function accomplishes two tasks:
                    - index each node into a string
                    - search the duplicated nodes during the traversal
            """
            nonlocal node_str_set
            nonlocal duplicated_strs
            nonlocal duplicated_nodes

            if node is None:
                return ""

            left_str = node2str(node.left)
            right_str = node2str(node.right)

            node_str = str(node.val) + "(" + left_str + ")" + "(" + right_str + ")"

            if node_str in node_str_set:
                if node_str not in duplicated_strs:
                    duplicated_strs.add(node_str)
                    duplicated_nodes.append(node)
            else:
                node_str_set.add(node_str)

            return node_str


        node2str(root)

        return duplicated_nodes







