

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
               construct a sliding window, where the left boundary 
                 is the index of the latest unseen char.
        """
        index_dict = {}
        start = 0
        max_size = 0
        for i, letter in enumerate(s):
            if letter in index_dict:
                start = max(index_dict[letter], start)

            index_dict[letter] = i+1

            max_size = max(i-start+1, max_size)

        return max_size


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

    test_case_1_input = ("abcabcbb", )
    test_case_1_target = 3
    verify('test case 1:',
           test_case_1_input, test_case_1_target,
           solution.lengthOfLongestSubstring)

    test_case_2_input = ("bbbbbbbb", )
    test_case_2_target = 1
    verify('test case 2:',
           test_case_2_input, test_case_2_target,
           solution.lengthOfLongestSubstring)

    test_case_3_input = ("", )
    test_case_3_target = 0
    verify('test case 3:',
           test_case_3_input, test_case_3_target,
           solution.lengthOfLongestSubstring)

    test_case_4_input = ("pwwkew", )
    test_case_4_target = 3
    verify('test case 4:',
           test_case_4_input, test_case_4_target,
           solution.lengthOfLongestSubstring)


    test_case_5_input = ("dvdf", )
    test_case_5_target = 3
    verify('test case 5:',
           test_case_5_input, test_case_5_target,
           solution.lengthOfLongestSubstring)


