
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_map = {"2": "abc", "3": "def", "4": "ghi", '5': "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        output = []

        def dfs(curr_index, comb):
            nonlocal output

            if curr_index == len(digits):
                output.append("".join(comb))
                return

            digit = digits[curr_index]
            for letter in digit_map[digit]:
                comb.append(letter)
                dfs(curr_index+1, comb)
                comb.pop()

        if len(digits) == 0:
            return []

        dfs(0, [])
        return output
