class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:

        p1, p2 = len(arr1)-1, len(arr2)-1
        carry = 0
        result = []

        while p1 >= 0 or p2 >= 0 or carry:

            bit_sum = 0

            if p1 >= 0:
                bit_sum += arr1[p1]
                p1 -= 1

            if p2 >= 0:
                bit_sum += arr2[p2]
                p2 -= 1

            bit_sum += carry
            result.append(bit_sum % 2)

            # the difference between base 2 and base -2
            # The parenthese (bit_sum // 2) is absolutely necessary!
            carry = - (bit_sum // 2)

        # remove the leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]
