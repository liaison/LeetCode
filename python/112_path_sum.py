class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, remain):
            # leaf node
            if node.left is None and node.right is None:
                return remain == node.val

            for child in [node.left, node.right]:
                if child and dfs(child, remain - node.val):
                    return True
            return False


        if not root:
            return False
        return dfs(root, targetSum)


