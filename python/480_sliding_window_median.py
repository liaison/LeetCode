class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        window, medians = [], []
        for i, num in enumerate(nums):

            # insert an element into sorted list
            # the resulting list would be still in order
            bisect.insort(window, num)

            if i >= k:
                # remove the element that is just out of scope
                # window.remove(nums[i-k])
                # apply binary search to locate the element to remove
                # but it won't make much difference, since eventually
                #   we need to shift the elements
                window.pop(bisect.bisect(window, nums[i-k]) - 1)

            if i >= k - 1:
                if k  % 2 == 0:
                    median = (window[k//2] + window[k//2 - 1]) / 2
                else:
                    median = window[k//2]

                medians.append(median)


        return medians