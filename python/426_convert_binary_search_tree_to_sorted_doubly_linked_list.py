
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None

        """
            Convert a BST tree to a doubly-linked list
            return the head and tail of the list
        """
        def head_and_tail_of_list(node):
            if not node:
                return None, None

            if node.left:
                left_head, left_tail = head_and_tail_of_list(node.left)
                left_tail.right = node
                node.left = left_tail
            else:
                left_head = node

            if node.right:
                right_head, right_tail = head_and_tail_of_list(node.right)
                node.right = right_head
                right_head.left = node
            else:
                right_tail = node

            return left_head, right_tail

        head, tail = head_and_tail_of_list(root)
        # chain up head and tail
        head.left = tail
        tail.right = head

        return head


