"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        
        sorted_counts = sorted(numCount.items(), key=lambda kv: kv[1])
        
        return [sorted_counts[-i][0] for i in range(1, k+1)]

class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #cnt = collections.Counter(nums)
        #return [kv[0] for kv in cnt.most_common(k)]
        
        cnt = collections.Counter(nums)
        
        import heapq
        return heapq.nlargest(k, cnt, key=cnt.get)

class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = collections.Counter(nums)
        return [kv[0] for kv in cnt.most_common(k)]