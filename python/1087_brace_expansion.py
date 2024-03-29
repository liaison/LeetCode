class SolutionStrManipulation:
    def expand(self, S: str) -> List[str]:

        blocks = S.replace("{", " ").replace("}", " ").strip().split()
        dict_list = [sorted(block.split(',')) for block in blocks]

        results = []

        def backtrack(curr, comb):
            if curr == len(dict_list):
                results.append("".join(comb))
                return

            for letter in dict_list[curr]:
                comb[curr] = letter
                backtrack(curr+1, comb)

        comb = [""] * len(dict_list)
        backtrack(0, comb)

        return results

class SolutionRegex:
    def expand(self, s: str) -> List[str]:

        import re
        str_list = re.split("[\{\}]", s)
        levels = [sorted(string.split(',')) for string in str_list]

        output = []
        end_level = len(levels)
        def dfs(curr_level, comb):
            nonlocal output

            if curr_level == end_level:
                output.append("".join(comb))
                return

            for candidate in levels[curr_level]:
                comb.append(candidate)
                dfs(curr_level + 1, comb)
                comb.pop()

        dfs(0, [])

        return output


class Solution:
    def expand(self, S: str) -> List[str]:

        dict_list = []

        curr = 0
        while curr < len(S):
            if S[curr] == "{":
                curr += 1
                start_bracket = curr
                while S[curr] != "}":
                    curr += 1
                options = S[start_bracket:curr].split(",")
                dict_list.append(sorted(options))
            else:
                dict_list.append([S[curr]])
            curr += 1

        results = []

        def backtrack(curr, comb):
            if curr == len(dict_list):
                results.append("".join(comb))
                return

            for letter in dict_list[curr]:
                comb[curr] = letter
                backtrack(curr+1, comb)

        comb = [""] * len(dict_list)
        backtrack(0, comb)

        return results
