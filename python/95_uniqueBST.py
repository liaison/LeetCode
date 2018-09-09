"""
Given an integer n, generate all structurally unique BST's (binary search trees)
  that store values 1 ... n.

Example: 

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 10, 2018

"""


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def to_list_inorder(root):
    if (root == None):
        return [None]
    
    # leaf node
    if (root.left == None and root.right == None):
        return [root.val]

    ret = [root.val]
    ret.extend(to_list_inorder(root.left))
    ret.extend(to_list_inorder(root.right))
    return ret


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        pass



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

    #test_case_1_input = (3, )
    #test_case_1_target = 5
    #verify('test case 1:',
    #       test_case_1_input, test_case_1_target, solution.generateTrees)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n2.right = n3
    n1.right = n2
    #n2.left = n1
    #n2.right = n3

    print(to_list_inorder(n1))



