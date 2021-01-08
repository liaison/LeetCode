class Solution:
    def isAdditiveNumber(self, num: str) -> bool:


        def dfs(prev_sum_str, prev_num_str, start, count):

            if start > len(num) - 1:
                return True if count >= 3 else False
            elif len(num) - start + 1 < len(prev_sum_str):
                return False
            elif num[start:(start+len(prev_sum_str))] != prev_sum_str:
                return False
            else:
                next_start = start + len(prev_sum_str)
                next_sum = int(prev_sum_str) + int(prev_num_str)
                return dfs(str(next_sum), prev_sum_str, next_start, count+1)


        for first_sep in range(1, len(num)-1):
            first_num = int(num[0:first_sep])
            # skip the numbers with leading zero, e.g. "02"
            if first_sep > 1 and first_num < 10:
                break

            for second_sep in range(first_sep+1, len(num)):
                prev_num = int(num[first_sep:second_sep])
                # skip the numbers with leading zero, e.g. "02"
                if second_sep - first_sep > 1 and prev_num < 10:
                    break

                prev_sum = first_num + prev_num
                if dfs(str(prev_sum), str(prev_num), second_sep, 2):
                    return True

        return False





