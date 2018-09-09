"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example: 

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 9, 2018

"""

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        
        return G[n]


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

    test_case_1_input = (3, )
    test_case_1_target = 5
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.numTrees)






