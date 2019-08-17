"""
Given the root of a binary tree, find the maximum value V for which 
there exists different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: 
any child of A is equal to B, or any child of A is an ancestor of B.)

"""
class Solution1:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """Time limit exceeded solution
        """
        maxDiff = float('-inf')
        def dfs(node, ancestors):
            nonlocal maxDiff
            
            if node is None:
                return
            
            for ancestor in ancestors:
                diff = abs(node.val - ancestor.val)
                maxDiff = max(diff, maxDiff)
            
            newAncestors = ancestors + [node]
            dfs(node.left, newAncestors)
            dfs(node.right, newAncestors)
        
        dfs(root, [])
        
        return maxDiff


class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        maxDiff = float('-inf')
        
        def dfs(node, extremeAncestors):
            nonlocal maxDiff
            
            if node is None:
                return
            
            for value in extremeAncestors:
                diff = abs(node.val - value)
                maxDiff = max(diff, maxDiff)
            
            minAncestor, maxAncestor = extremeAncestors
            
            newXAncestors = (min(minAncestor, node.val),
                             max(maxAncestor, node.val))
            dfs(node.left, newXAncestors)
            dfs(node.right, newXAncestors)
        
        dfs(root, (root.val, root.val))
        
        return maxDiff


class SolutionOptimal:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def minMaxDfs(node, low, high):
            """
                find the min/max values along the path
            """
            if not node:
                # the extreme difference can only be between the extreme values !
                return (high-low)
            
            low = min(node.val, low)
            high = max(node.val, high)
            return max(minMaxDfs(node.left, low, high),
                       minMaxDfs(node.right, low, high))

        if not root: return 0

        return minMaxDfs(root, root.val, root.val)
            
