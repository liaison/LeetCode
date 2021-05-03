class Solution:
    def grayCode(self, n: int) -> List[int]:

        res = []

        if n == 0:
            return [0]

        res.append(0)
        res.append(1)

        shift = 1
        while shift < n:

            size = len(res)
            for i in range(size-1, -1, -1):
                new_value = res[i] | (1 << shift)
                res.append(new_value)

            shift += 1

        return res
