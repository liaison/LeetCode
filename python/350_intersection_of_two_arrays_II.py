
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0

        nums1_len, nums2_len = len(nums1), len(nums2)

        result = []
        while p1 < nums1_len and p2 < nums2_len:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
            elif nums1[p1] > nums2[p2]:
                p1 -= 1
            else:
                p2 -= 1

            p1 += 1
            p2 += 1

        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # https://www.geeksforgeeks.org/operations-on-python-counter/
        # Operations on Counter:  +, -, &, |
        #   addition, subtraction, intersection, union
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        result = []

        # intersections between the frequency count
        intersections = counter1 & counter2
        for key, count in intersections.items():
            result.extend([key] * count)

        return result
