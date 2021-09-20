# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest_node = root
        # traverse the BST in the order of binary search
        #   check every node that we traverse.
        while root:
            closest_node = min(root, closest_node, key = lambda x: abs(target - x.val))

            # next iteration
            root = root.left if target < root.val else root.right

        return closest_node.val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        curr = root
        closest_node = root
        min_value = float('inf')

        while curr:
            diff = abs(curr.val - target)
            if diff < min_value:
                min_value = diff
                closest_node = curr

            if curr.val < target:
                curr = curr.right
            else:
                curr = curr.left

        return closest_node.val
