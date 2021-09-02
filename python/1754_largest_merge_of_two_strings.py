class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        index_1, index_2 = 0, 0
        len_1, len_2 = len(word1), len(word2)

        merge = []
        while index_1 < len_1 or index_2 < len_2:

            # one of the pointers reaches the end
            if index_1 == len_1:
                merge.append(word2[index_2])
                index_2 += 1
            elif index_2 == len_2:
                merge.append(word1[index_1])
                index_1 += 1
             # both pointers are still within the boundary
            else:
                # pick the larger letter
                if word1[index_1] > word2[index_2]:
                    merge.append(word1[index_1])
                    index_1 += 1
                elif word1[index_1] < word2[index_2]:
                    merge.append(word2[index_2])
                    index_2 += 1
                else:
                    # look ahead of the rest of the substring
                    if word1[index_1:] >= word2[index_2:]:
                        merge.append(word1[index_1])
                        index_1 += 1
                    else:
                        merge.append(word2[index_2])
                        index_2 += 1

        return "".join(merge)




