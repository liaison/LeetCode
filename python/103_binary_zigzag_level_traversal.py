"""

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level
 and alternate between).

@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 22, 2018

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder_deque(self, root):
        ret = []
        level_list = []
        if root is None:
            return []

        from collections import deque
        node_queue = deque([root, None])

        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                level_list.append(curr_node.val)
            
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # level sentinel
                if not is_order_left:
                    level_list.reverse()
                ret.append(level_list)
                level_list = []
                is_order_left = not is_order_left # change the order

                if len(node_queue) > 0:
                    node_queue.append(None)

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
    test_case_1_target = [[1], [3, 2]]
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
           test_case_3_input, test_case_3_target, solution.levelOrder_deque)
    

    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p2.left = p3
    p3.left = p4
    p3.right = p5
    test_case_4_input = (p1, )
    test_case_4_target = [[1], [2], [3], [5,4]]
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.levelOrder_deque)

