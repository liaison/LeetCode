import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.prefix_sums = []
        self.total_area = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            # the area could be of lines
            area = (x2-x1 + 1) * (y2-y1 + 1)
            self.total_area += area
            self.prefix_sums.append(self.total_area)
        self.rects = rects

    def pick(self) -> List[int]:
        
        pick = int(random.random() * self.total_area)        
        
        # binary search to locate the chosen rectangle
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = int((high - low) / 2 + low)
            if pick >= self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        
        picked_rect = self.rects[low]
        x1, y1, x2, y2 = picked_rect
        
        return [random.randrange(x1, x2+1), random.randrange(y1, y2+1)] 


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()