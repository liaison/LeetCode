# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        path_list = []
        def backtrack(node, path, remaining):
            nonlocal path_list

            if node is None:
                # early return
                return

            if node.left is None and node.right is None:
                # leaf node
                if remaining == node.val:
                    good_path = path.copy()
                    good_path.append(node.val)
                    path_list.append(good_path)
                    return

            for child in [node.left, node.right]:
                if child:
                    path.append(node.val)
                    backtrack(child, path, remaining - node.val)
                    path.pop()


        backtrack(root, [], targetSum)

        return path_list
