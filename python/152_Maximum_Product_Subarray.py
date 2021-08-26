
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            Keep the intermediate results of the previous num
        """
        curr_products = []
        max_product = float('-inf')

        for num in nums:
            curr_products.append(1)
            next_products = []
            for product in curr_products:
                new_product = num * product
                max_product = max(max_product, new_product)
                next_products.append(new_product)

            curr_products = next_products

        return max_product


class SolutionDP:
    """
        Rather than keeping all the intermediate products,
          we take the two extreme numbers among the intermediate results,
          since only these two extreme numbers can change the final result.
    """
    def maxProduct(self, nums: List[int]) -> int:

        max_product = nums[0]
        max_sofar, min_sofar = nums[0], nums[0]

        for num in nums[1:]:
            new_min_sofar = num * min_sofar
            new_max_sofar = num * max_sofar
            min_sofar = min(num, new_min_sofar, new_max_sofar)
            max_sofar = max(num, new_min_sofar, new_max_sofar)

            max_product = max(max_product, max_sofar)

        return max_product