class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        index_1, index_2 = 0, 0
        len_1, len_2 = len(word1), len(word2)

        merge = []
        while index_1 < len_1 or index_2 < len_2:

            if index_1 == len_1:
                merge.append(word2[index_2])
                index_2 += 1
            elif index_2 == len_2:
                merge.append(word1[index_1])
                index_1 += 1
            else: # both index are valid
                # look ahead of the rest of the substring
                # pick the larger substring
                if word1[index_1:] >= word2[index_2:]:
                    merge.append(word1[index_1])
                    index_1 += 1
                else:
                    merge.append(word2[index_2])
                    index_2 += 1

        return "".join(merge)
