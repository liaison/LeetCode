class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        p1, p2 = len(num1) - 1, len(num2) - 1
        output = []
        carry = 0

        while p1 >= 0 or p2 >= 0:

            bit_sum = 0

            if p1 >= 0:
                bit_sum += int(num1[p1])
                p1 -= 1

            if p2 >= 0:
                bit_sum += int(num2[p2])
                p2 -= 1

            bit_sum += carry
            carry = bit_sum // 10
            curr_bit = bit_sum % 10

            output.append(str(curr_bit))

        if carry > 0:
            output.append(str(carry))

        return "".join(reversed(output))