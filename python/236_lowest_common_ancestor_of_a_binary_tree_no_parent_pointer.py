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
                # result = list(path)  WONT WORK !!!
                # One should operate within the object, but not reassign the pointer
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



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = None
        def get_descendants(node):
            """
                Retrieve all the descendant nodes starting from the input node.
                while traversing the nodes, find the first subtree that contains the two input nodes
            """
            nonlocal result

            if not node:
                return set()

            left_nodes = get_descendants(node.left)

            # we find the result in the left tree, early exit!
            if result:
                return set()

            right_nodes = get_descendants(node.right)

            all_nodes = left_nodes | right_nodes | {node.val}

            # the first subtree that contains both the target nodes
            if p.val in all_nodes and q.val in all_nodes and not result:
                result = node

            return all_nodes

        get_descendants(root)
        return result
