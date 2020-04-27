class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sum_array = []

        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum_array.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        from bisect import bisect_left

        prefix_sum = self.total_sum * random.random()
        return bisect_left(self.prefix_sum_array, prefix_sum)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()