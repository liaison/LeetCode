
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        str_bitmap = {}
        refined_array = []

        def str_to_bitmap(string):
            bitmap = 0
            for letter in string:
                next_bitmap = bitmap | (1 << (ord(letter) - ord('a')))
                if next_bitmap == bitmap:
                    return False, None
                bitmap = next_bitmap
            return True, bitmap

        # Filter out strings that contain duplicated characters
        # convert the string to its corresponding bitmap
        for string in arr:
            is_unique, bitmap = str_to_bitmap(string)
            if is_unique:
                refined_array.append(string)
                str_bitmap[string] = bitmap

        max_len = float('-inf')

        # generate all possible permutations
        def backtrack(curr_index, curr_bitmap, curr_len):
            nonlocal max_len

            max_len = max(max_len, curr_len)

            for next_index in range(curr_index, len(refined_array)):
                string = refined_array[next_index]

                # check there is no duplicate when appending a new string
                concat_bitmap = str_bitmap[string] | curr_bitmap
                check_bitmap = str_bitmap[string] ^ curr_bitmap

                if concat_bitmap == check_bitmap:
                    backtrack(next_index+1, concat_bitmap, curr_len + len(string))

        backtrack(0, 0, 0)

        return max_len



