# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        def symmetric(left, right):
            if left and right:
                if left.val == right.val:
                    if symmetric(left.left, right.right):
                        return symmetric(left.right, right.left)
                return False
            elif left is None and right is None:
                return True
            else:
                return False

        return symmetric(root.left, root.right)



class SolutionBFS:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        # BFS traversal
        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if left and right:
                if left.val != right.val:
                    return False
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
            elif left is None and right is None:
                continue
            else:
                return False

        return True

