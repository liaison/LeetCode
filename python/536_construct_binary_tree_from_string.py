# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:

        if s == "":
            return None

        s_len = len(s)

        def get_number():
            index = 0
            while index < s_len:
                if s[index] == '(':
                    break
                index += 1
            num = int("".join(s[0:index]))
            return index, num

        index, num = get_number()
        node = TreeNode(val=num)

        def get_substr(start):
            """
                Retrieve a substring in the pattern of "(...)"
            """
            index = start
            parenthesis_cnt = 0
            while index < s_len:
                if s[index] == '(':
                    parenthesis_cnt += 1
                elif s[index] == ')':
                    parenthesis_cnt -= 1

                if parenthesis_cnt == 0:
                    break
                index += 1

            return s[start:index+1]


        left_substr = get_substr(index)
        left_node = self.str2tree(left_substr[1:-1])

        right_substr = get_substr(index + len(left_substr))
        right_node = self.str2tree(right_substr[1:-1])

        node.left = left_node
        node.right = right_node
        return node











