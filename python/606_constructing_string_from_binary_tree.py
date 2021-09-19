# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def node_to_str(node):

            if node is None:
                return ""

            result_list = [str(node.val)]

            left_str = node_to_str(node.left)
            right_str = node_to_str(node.right)

            if left_str == "":
                if right_str != "":
                    result_list.append("()")
            else:
                result_list.append("(")
                result_list.append(left_str)
                result_list.append(")")

            if right_str != "":
                result_list.append("(")
                result_list.append(right_str)
                result_list.append(")")

            return "".join(result_list)


        return node_to_str(t)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRefined:
    def tree2str(self, t: TreeNode) -> str:

        def node_to_str(node):
            if node is None:
                return ""

            result_list = [str(node.val)]

            left_str = node_to_str(node.left)
            right_str = node_to_str(node.right)

            if len(left_str) > 0 or len(right_str) > 0:
                result_list.append("(" + left_str + ")")

            if len(right_str) > 0:
                result_list.append("(" + right_str + ")")

            return "".join(result_list)


        return node_to_str(t)




