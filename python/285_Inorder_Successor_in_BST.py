# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionBinarySearch:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        curr = root
        candidate = None
        
        # Binary Search traversal
        while curr:
            if curr.val > p.val:
                # update candidate with the latest value that is greater than P
                candidate = curr
                curr = curr.left
            else: # curr.val <= p.val
                curr = curr.right
        
        return candidate


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        result = None
        
        # stack with a pseudo head
        stack = [None]
        
        def inorderDFS(node):
            nonlocal result
            
            if not node:
                return
            
            inorderDFS(node.left)
            
            # if the previous element is the target element
            prev = stack.pop()
            if prev == p:
                result = node
            stack.append(node)
            
            inorderDFS(node.right)
            
        inorderDFS(root)
        
        return result
