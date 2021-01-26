# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        queue = deque([root])
        avg_list = []
        while queue:
            level_size = len(queue)

            level_sum = 0
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                for next_node in [node.left, node.right]:
                    if next_node is not None:
                        queue.append(next_node)

            avg_list.append(level_sum / level_size)

        return avg_list
