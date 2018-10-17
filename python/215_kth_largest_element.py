"""


@author: Lisong Guo <lisong.guo@me.com>
@date:   Sep 23, 2018

"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]


    def findKthLargest_linear(self, nums, k):
        """ """
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        
        def swap(a, b):
            print('swap({} {})'.format(a,b))
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        print("k:{} nums:{}".format(k, nums))

        k -= 1

        while low < high:
            # sort of bubble sort
            pivot = nums[k]
            left = low
            right = high

            print('@@@ k:{} pivot:{} low:{}, high:{}, nums:{}'.format(
                    k, pivot, low, high, nums))
            
            # quick selection
            # left handside numbers  > nums[k]
            # right handside numbers < nums[k]
            while True:
                while nums[left] > pivot: left += 1
                while nums[right] < pivot: right -= 1
                
                if left <= right:
                    swap(left, right)
                    left += 1
                    right -= 1

                if left > right: break

            print('### k:{} pivot:{} low:{}, high:{}, nums:{}'.format(
                    k, pivot, low, high, nums))
            
            # narrow down the sorting zone
            if left > k: high = right
            if right < k: low = left


        return nums[k]


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
    
    t1 = [3,3,3,3,4,3,3,3,3]
    k1 = 5
    test_case_1_input = (t1, k1)
    test_case_1_target = 3
    #verify('test case 1:',
    #       test_case_1_input, test_case_1_target, solution.findKthLargest)
    verify('test case 1:',
           test_case_1_input, test_case_1_target, solution.findKthLargest_linear)

    t2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    test_case_2_input = (t2, k2)
    test_case_2_target = 4
    #verify('test case 2:',
    #       test_case_2_input, test_case_2_target, solution.findKthLargest)
    verify('test case 2:',
           test_case_2_input, test_case_2_target, solution.findKthLargest_linear)

    
    t3 = [1]
    k3 = 1
    test_case_3_input = (t3, k3)
    test_case_3_target = 1
    verify('test case 3:',
           test_case_3_input, test_case_3_target, solution.findKthLargest_linear)
    
    t4 = [-1, 2, 0]
    k4 = 1
    test_case_4_input = (t4, k4)
    test_case_4_target = 2
    verify('test case 4:',
           test_case_4_input, test_case_4_target, solution.findKthLargest_linear)
    
    t5 = [2, 1]
    k5 = 2
    test_case_5_input = (t5, k5)
    test_case_5_target = 1
    verify('test case 5:',
           test_case_5_input, test_case_5_target, solution.findKthLargest_linear)
    
    t6 = [1, 2, 3, 4, 5, 6]
    k6 = 1
    test_case_6_input = (t6, k6)
    test_case_6_target = 6
    verify('test case 6:',
           test_case_6_input, test_case_6_target, solution.findKthLargest_linear)

    t7 = [5,2,4,1,3,6,0]
    k7 = 2
    test_case_7_input = (t7, k7)
    test_case_7_target = 5
    verify('test case 7:',
           test_case_7_input, test_case_7_target, solution.findKthLargest_linear)

    
    t8 = [3,3,3,3,3,3,3,3,3]
    k8 = 8
    test_case_8_input = (t8, k8)
    test_case_8_target = 3
    verify('test case 8:',
           test_case_8_input, test_case_8_target, solution.findKthLargest_linear)



