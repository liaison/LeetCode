
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

        index = 0
        s_len = len(s)
        num_str = []
        while index < s_len:
            if s[index] != '(':
                num_str.append(s[index])
            else:
                break
            index += 1

        num = int("".join(num_str))
        node = TreeNode(val=num)

        # retrieve the next block of "(substr)"
        def get_substr(index):
            substr = []
            parenthesis_cnt = 0
            while index < s_len:
                if s[index] == '(':
                    parenthesis_cnt += 1
                elif s[index] == ')':
                    parenthesis_cnt -= 1
                substr.append(s[index])

                if parenthesis_cnt == 0:
                    break
                index += 1
            return "".join(substr)


        left_substr = get_substr(index)
        left_node = self.str2tree(left_substr[1:-1])

        right_substr = get_substr(index + len(left_substr))
        right_node = self.str2tree(right_substr[1:-1])

        node.left = left_node
        node.right = right_node
        return node

