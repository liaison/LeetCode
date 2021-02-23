
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modulo = 10**9 + 7

        @functools.lru_cache(maxsize=None)
        def count_ways(array_index, max_num, remain_cost):

            if array_index == n:
                if remain_cost == 0:
                    return 1
                else:
                    return 0

            count = 0
            for num in range(1, m+1):
                if num > max_num:
                    count += count_ways(array_index+1, num, remain_cost - 1)
                else:
                    count += count_ways(array_index+1, max_num, remain_cost)

                count = count % modulo

            return count

        ans = 0
        for num in range(1, m+1):
            ans = (ans + count_ways(1, num, k-1)) % modulo

        return ans

