# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.value_set = set()

        def populate(node, value):
            if node is None:
                return

            node.val = value
            self.value_set.add(value)
            populate(node.left, 2 * value + 1)
            populate(node.right, 2 * value + 2)

        populate(root, 0)
        self.root = root

    def find(self, target: int) -> bool:

        # def dfs(node):
        #     if node is None:
        #         return False
        #     if target == node.val:
        #         return True
        #     if dfs(node.left):
        #         return True
        #     return dfs(node.right)

        return (target in self.value_set)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)