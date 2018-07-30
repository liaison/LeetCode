"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

@author: Lisong Guo <lisong.guo@me.com>
@date:   July 30, 2018

"""

class Solution:
    def _search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

            recursive binary search in all sub-trees
        """
        size = len(nums)
        mid = int(size/2)

        if (size == 0):
           return -1

        if (nums[mid] == target):
            return mid
        else:
            # check the left subtree
            left_ret = self.search(nums[0:mid], target)
            if (left_ret != -1):
                return left_ret
            else:
                # if not found solution in left subtree, check right subtree
                right_ret = self.search(nums[mid+1:], target)
                if (right_ret != -1):
                    return mid + 1 + right_ret
                else:
                    return -1


    def search(self, nums, target):
        """
            a revised binary search, at each step we are still able to narrow 
              down to the right side.
        """
        start = 0
        end = len(nums)
        
        import sys

        while (start < end):
            mid = int((start+end)/2)

            if (target == nums[mid]):
                return mid

            same_side = ((target < nums[0]) == (nums[mid] < nums[0]))

            if (not same_side):
                comparator = -sys.maxsize-1 if (target < nums[0]) else sys.maxsize
            else:
                comparator = nums[mid]

            if (target > comparator):
                start = mid + 1
            else:
                end = mid


        return -1


    def binary_search(self, sorted_nums, target):
        """
        """
        start = 0
        end = len(sorted_nums) - 1

        while (start <= end):
            mid = int((start+end)/2)
            if (sorted_nums[mid] == target):
                return mid
            elif (sorted_nums[mid] < target):
                start = mid + 1
            else:
                end = mid - 1

        # did not find the target
        return -1


def verify(case_name, test_input, test_target, test_func):
    """
       utility function for unit testing
    """
    print(case_name, test_input, ' target:', test_target)
    assert(test_target == test_func(*test_input))


if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = ([4,5,6,7,0,1,2], 4)
    test_case_1_target = 0
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.search)

    test_case_2_input = ([4,5,6,7,0,1,2], 3)
    test_case_2_target = -1
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.search)
    
    test_case_4_input = ([4,5,6,7,0,1,2], 6)
    test_case_4_target = 2
    print(solution.search(*test_case_4_input))
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.search)
    
    test_case_5_input = ([4,5,6,7,0,1,2], 0)
    test_case_5_target = 4
    print(solution.search(*test_case_5_input))
    verify('test case 5:',
           test_case_5_input, test_case_5_target, solution.search)

    sorted_list_1 = [x for x in range(5)]
    test_case_3_input = (sorted_list_1, 2)
    test_case_3_target = 2
    verify('test case 1 for binary search:',
           test_case_3_input, test_case_3_target, solution.binary_search)
       



