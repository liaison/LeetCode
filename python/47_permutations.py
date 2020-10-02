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
            # check if nums[end] in the list of nums[start:end]
            return nums[end] in nums[start:end]

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


    def permuteUnique_vt(self, nums):
        """ solution with visit_table
        """
        ret = []
        visited = [0] * len(nums)
        nums.sort()

        def permute_dfs(path):
            print('visit:{} path:{}'.format(visited, path))
            if len(path) == len(nums):
                ret.append(path)
                return
            
            for i in range(0, len(nums)):
                print(visited)

                if visited[i] == 1: continue
                if i > 0 and visited[i-1] == 0 and nums[i] == nums[i-1]: continue
                visited[i] = 1
                permute_dfs(path + [nums[i]])
                visited[i] = 0

        permute_dfs([])
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

    #verify('test case 1:',
    #       test_case_1_input, test_case_1_target, solution.permuteUnique)

    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.permuteUnique_vt)
    
    t2 = [2, 2, 1, 1]
    test_case_2_input = (t2, )
    test_case_2_target = [[2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2],
                          [1, 2, 2, 1], [1, 2, 1, 2], [1, 1, 2, 2]]
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.permuteUnique)
