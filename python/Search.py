class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        mid = int(size/2)

        if (size == 0):
           return -1

        if (nums[mid] == target):
            return mid
        else:
            left_ret = self.search(nums[0:mid], target)
            if (left_ret != -1):
                return left_ret
            else:
                right_ret = self.search(nums[mid+1:], target)
                if (right_ret != -1):
                    return mid + 1 + right_ret
                else:
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


def verify(case_name, test_input, test_target):
    """
       utility function for unit testing
    """
    solution = Solution()
    print(case_name, test_input, ' target:', test_target)
    assert(test_target == solution.search(*test_input))


if __name__ == "__main__":

    solution = Solution()

    test_case_1_input = ([4,5,6,7,0,1,2], 4)
    test_case_1_target = 0
    verify('test case 1:', test_case_1_input, test_case_1_target)


    test_case_2_input = ([4,5,6,7,0,1,2], 3)
    test_case_2_target = -1
    verify('test case 2:', test_case_2_input, test_case_2_target)
    

    sorted_list_1 = [x for x in range(5)]
    target = 2
    print(sorted_list_1, target)
    print(solution.binary_search(sorted_list_1, target))
       



