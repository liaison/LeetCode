# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def isIdentical(a, b):
            if a is None or b is None:
                return (a is None) and (b is None)
            if a.val != b.val:
                return False
            if not isIdentical(a.left, b.left):
                return False
            return isIdentical(a.right, b.right)
        
        if s is None:
            return False
        
        if s.val == t.val:
            if isIdentical(s, t):
                return True
        
        if self.isSubtree(s.left, t):
            return True
        else:
            return self.isSubtree(s.right, t)
