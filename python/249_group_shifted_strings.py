
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        str_table = defaultdict(list)

        for string in strings:
            str_len = len(string)
            if str_len == 1:
                str_table[(1)].append(string)
            else:
                #  list of distances between each adjacent letters
                key = []
                for index in range(1, str_len):
                    diff = (ord(string[index]) - ord(string[index-1]) + 26) % 26
                    key.append(diff)

                str_table[tuple(key)].append(string)

        return str_table.values()
