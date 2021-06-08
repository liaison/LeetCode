class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def common_prefix(word_1, word_2):
            bound = min(len(word_1), len(word_2))
            index = 0
            while index < bound:
                if word_1[index] != word_2[index]:
                    break
                index += 1

            return word_1[0:index]

        prefix = strs[0]
        for word in strs[1:]:
            prefix = common_prefix(prefix, word)

        return prefix
