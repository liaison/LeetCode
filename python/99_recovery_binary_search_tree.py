# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first_switch, second_switch = None, None
        prev_node = None

        def dfs(curr_node):
            nonlocal first_switch, second_switch, prev_node
            if not curr_node:
                return

            # inorder travesal
            dfs(curr_node.left)

            if prev_node:
                if curr_node.val < prev_node.val:
                    second_switch = curr_node
                    if not first_switch:
                        first_switch = prev_node
                    else:
                        return
            # prev_node need to be global
            prev_node = curr_node

            dfs(curr_node.right)

        dfs(root)

        first_switch.val, second_switch.val = second_switch.val, first_switch.val



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionIteration:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first_switch, second_switch = None, None
        prev = None

        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev and prev.val > curr.val:
                second_switch = curr
                if not first_switch:
                    first_switch = prev
                else:
                    break

            prev = curr

            curr = curr.right

        first_switch.val, second_switch.val = second_switch.val, first_switch.val



