
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_node_cnt = 0
        def dfs(node, max_value):
            nonlocal good_node_cnt

            if not node:
                return

            if node.val >= max_value:
                good_node_cnt += 1

            new_max_value = max(max_value, node.val)
            dfs(node.left, new_max_value)
            dfs(node.right, new_max_value)

        dfs(root, float('-inf'))

        return good_node_cnt


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFSwithStack:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes_cnt = 0

        stack = [(root, float('-inf'))]

        while stack:
            curr, max_sofar = stack.pop()

            if max_sofar <= curr.val:
                good_nodes_cnt += 1
                max_sofar = curr.val

            for next_node in [curr.left, curr.right]:
                if next_node:
                    stack.append((next_node, max_sofar))

        return good_nodes_cnt


