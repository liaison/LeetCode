class SolutionHashTableNaive:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        num_index1 = defaultdict(list)
        for index1, num in enumerate(nums1):
            num_index1[num].append(index1)

        max_len = 0

        for index2, num in enumerate(nums2):

            for index1 in num_index1[num]:
                new_len = 0
                p1, p2 = index1, index2
                while p1 < len(nums1) and p2 < len(nums2) and nums1[p1] == nums2[p2]:
                    new_len += 1
                    p1 += 1
                    p2 += 1

                max_len = max(max_len, new_len)

            # early break, but still TLE
            if max_len in [len(nums1), len(nums2)]:
                break

        return max_len