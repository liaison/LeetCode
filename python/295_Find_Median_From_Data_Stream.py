class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        median_index = len(self.nums) // 2

        if len(self.nums) % 2 == 0:
            return (self.nums[median_index] + self.nums[median_index-1]) / 2
        else:
            return self.nums[median_index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
