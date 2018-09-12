"""
Serialization is the process of converting a data structure or object into a 
sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.

@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 12, 2018

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def rserialize(self, root, string):
        """ a recursive helper function for the serialize() function.
        :type root: TreeNode
        :type string: str
        :rtype: str
        """
        # check base case
        if root is None:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = self.rserialize(root.left, string)
            string = self.rserialize(root.right, string)
        return string

    def serialize(self, root):
        """ Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.rserialize(root, '')


    def rdeserialize(self, l, index):
        """Recursive deserialization.
        :type l: list
        :type index: integer
        :rtype: TreeNode
        """
        index += 1
        root = None

        # check base cases
        if (l[index - 1] != 'None'):
            root = TreeNode(l[index - 1])
            root.left, index = self.rdeserialize(l, index)
            root.right, index = self.rdeserialize(l, index)
        return root, index

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self.rdeserialize(data_list, 0)[0]



def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    actual_output = test_func(*test_input)
    print(case_name, test_input, ' target:', test_target,
          ' output:', actual_output)
    assert(test_target == actual_output)


if __name__ == "__main__":

    codec = Codec()

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3

    test_case_1_input = (t1, )
    test_case_1_target = "1,2,None,None,3,None,None,"
    verify('test case 1:',
           test_case_1_input, test_case_1_target, codec.serialize)


    test_case_2_input = (codec.serialize(None), )
    test_case_2_target = None
    verify('test case 2:',
           test_case_2_input, test_case_2_target, codec.deserialize)
    

    c3_root = TreeNode(1)
    test_case_3_input = (c3_root, )
    test_case_3_target = "1,None,None,"
    verify('test case 3:',
           test_case_3_input, test_case_3_target, codec.serialize)






