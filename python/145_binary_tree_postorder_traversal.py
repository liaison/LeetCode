# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            output.append(node.val)

        dfs(root)
        return output


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionStack:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = deque([])

        stack = [root]
        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                output.appendleft(node.val)

        return output
