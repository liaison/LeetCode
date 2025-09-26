

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        """
            Exceed the time limit
        """
        def common_prefix(str_a, str_b):
            min_len = min(len(str_a), len(str_b))
            index = 0
            while index < min_len:
                if str_a[index] != str_b[index]:
                    break
                index += 1
            return str_a[:index]

        max_len = 0

        for one in arr1:
            for other in arr2:

                prefix = common_prefix(str(one), str(other))

                max_len = max(max_len, len(prefix))

        return max_len


    def longestCommonPrefix_set(self, arr1: List[int], arr2: List[int]) -> int:
        """
            Build a set of prefix from one string array,
                to trade time with space
        """

        prefix_set = set()
        for one in arr1:
            one_str = str(one)
            for index in range(1, len(one_str)+1):
                prefix = one_str[:index]
                prefix_set.add(prefix)

        max_len = 0
        for other in arr2:
            other_str = str(other)
            for index in range(1, len(other_str)+1):
                prefix = other_str[:index]
                if prefix in prefix_set:
                    max_len = max(max_len, len(prefix))

        return max_len



solution = Solution()



print(solution.longestCommonPrefix([1, 10, 100], [1000]))
