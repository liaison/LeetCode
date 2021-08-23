

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_len = len(nums)
        prefix_products, postfix_products = [1] * (num_len + 1), [1] * (num_len + 1)

        prefix_product, postfix_product = 1, 1

        for prefix_index in range(num_len):
            prefix_product *= nums[prefix_index]
            prefix_products[prefix_index+1] = prefix_product

            postfix_index = num_len - 1 - prefix_index
            postfix_product *= nums[postfix_index]
            postfix_products[postfix_index] = postfix_product

        infix_products = []
        for index in range(num_len):
            infix_products.append(prefix_products[index] * postfix_products[index+1])

        return infix_products

