"""
@author: Lisong Guo <lisong.guo@me.com>
@date:   Oct 17, 2018

"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def swap(i, j):
            if i == j: return
            print('swap({},{})'.format(i,j))
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def isduplicate(start, end):
            for i in range(start, end):
                if nums[i] == nums[end]:
                    return True
            return False

        def permute_rec(start):
            if start == len(nums)-1:
                ret.append(nums.copy())
                return

            for i in range(start, len(nums)):
                if not isduplicate(start, i):
                    swap(start, i)
                    permute_rec(start+1)
                    swap(start, i)
            
        permute_rec(0)
        
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
    
    t1 = [1, 1, 2]
    test_case_1_input = (t1, )
    test_case_1_target = [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]

    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.permuteUnique)

    
    t2 = [2, 2, 1, 1]
    test_case_2_input = (t2, )
    test_case_2_target = [[2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2],
                          [1, 2, 2, 1], [1, 2, 1, 2], [1, 1, 2, 2]]
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.permuteUnique)
