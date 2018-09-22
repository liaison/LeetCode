"""

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 22, 2018

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        curr_level_node = [root]
        next_level_node = []
        value_list = []
        ret = []
        while len(curr_level_node) > 0:
            for node in curr_level_node:
                if node is not None:
                    value_list.append(node.val)
                    if node.left is not None:
                        next_level_node.append(node.left)
                    if node.right is not None:
                        next_level_node.append(node.right)
           
            if (len(value_list) == 0):
                break
            ret.append(value_list)
            curr_level_node = next_level_node
            value_list = []
            next_level_node = []

        return ret

    def levelOrder_deque(self, root):
        ret = []
        level_list = []
        if root is None:
            return []

        node_queue = [root, None]

        while len(node_queue) > 0:
            curr_node = node_queue.pop(0)
            if curr_node:
                level_list.append(curr_node.val)
            
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # level sentinel
                ret.append(level_list)
                level_list = []
                if len(node_queue) > 0:
                    node_queue.append(None)

        return ret


    def levelOrder_DFS(self, root):
        def levelOrder_DFS_rec(level, root):
            if root is not None:
                if level <= len(ret):
                    ret[level-1].append(root.val)
                else:
                    ret.append([root.val])

                levelOrder_DFS_rec(level+1, root.left)
                levelOrder_DFS_rec(level+1, root.right)

        ret = []
        levelOrder_DFS_rec(1, root)
        
        return ret


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


if __name__ == "__main__":

    solution = Solution()

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3

    test_case_1_input = (t1, )
    test_case_1_target = [[1], [2,3]]
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.levelOrder_deque)

    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.left = p2
    p2.left = p3

    test_case_2_input = (p1, )
    test_case_2_target = [[1], [2], [3]]
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.levelOrder_deque)


    test_case_3_input = (None, )
    test_case_3_target = []
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.levelOrder)

