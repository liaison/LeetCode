"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

  A binary tree in which the depth of the two subtrees of 
    every node never differ by more than 1.

@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 12, 2018

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_balanced_rec(self, root):
        if (root is None):
            return (True, 0)
        
        is_left, height_left = self.is_balanced_rec(root.left)
        if (not is_left):
            # we don't mind the height in case of unbalanced tree.
            return (False, -1)

        is_right, height_right = self.is_balanced_rec(root.right)
        if (not is_right):
            return (False, -1)
    
        if (abs(height_left-height_right) > 1):
            return (False, -1)
        else:
            return (True, max(height_left, height_right) + 1)


    def isBalanced(self, root):
        """
            :type root: TreeNode
            :rtype: bool
        """
        ret, height = self.is_balanced_rec(root)
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
    test_case_1_target = True
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.isBalanced)

    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.left = p2
    p2.left = p3

    test_case_2_input = (p1, )
    test_case_2_target = False
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.isBalanced)



