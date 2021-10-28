class Solution:
    def maximumSwap(self, num: int) -> int:
        # convert integer to a list of digits
        digits = []
        while num > 0:
            digit = num % 10
            digits.append(digit)
            num = num // 10
        digits.reverse()

        digits_len = len(digits)

        def swap(curr):
            if curr == digits_len - 1:
                return

            max_index = curr
            curr_max = digits[curr]
            for index in range(curr+1, digits_len):
                if curr_max <= digits[index]:
                    max_index = index
                    curr_max = digits[index]

            # if we did not find a suitable swap to perform, continue with the next digit
            if max_index == curr or digits[max_index] == digits[curr]:
                swap(curr+1)
            else:
                # swap the current digit with the maximum one in the rest of the digits
                digits[curr], digits[max_index] = digits[max_index], digits[curr]

        # greedily make a swap
        swap(0)

        # convert the list of digits back to an integer
        power = 1
        final_num = 0
        for digit in digits[::-1]:
            final_num += digit * power
            power *= 10

        return final_num