# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def dfs(node, path, target, result):
            """
                Build the path that leads to the target node
            """
            if node is None:
                return False

            if node == target:
                result.extend(list(path))
                return True

            is_found = False
            for next_node in [node.left, node.right]:
                path.append(next_node)
                is_found = dfs(next_node, path, target, result)
                path.pop()

                if is_found:
                    break

            return is_found

        path_to_p = []
        path_to_q = []
        dfs(root, [root], p, path_to_p)
        dfs(root, [root], q, path_to_q)

        # given the two paths, find the first branching point
        index = 0
        while True:
            if index >= len(path_to_p) or index >= len(path_to_q):
                break
            if path_to_p[index] != path_to_q[index]:
                break
            index += 1

        return path_to_p[index-1]

