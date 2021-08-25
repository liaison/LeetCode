
class SparseVector:
    def __init__(self, nums: List[int]):
        self.value_table = {}
        for index, num in enumerate(nums):
            if num != 0:
                self.value_table[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.value_table) < len(vec.value_table):
            small_table = self.value_table
            large_table = vec.value_table
        else:
            small_table = vec.value_table
            large_table = self.value_table

        dot_product = 0
        for key, value in small_table.items():
            if key in large_table:
                dot_product += value * large_table[key]

        return dot_product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)