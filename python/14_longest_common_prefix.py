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


    def longestCommonPrefix_dict(self, strs: List[str]) -> str:

        prefix_dict = defaultdict(int)

        def indexing_prefix(word):
            nonlocal prefix_dict
            for index in range(1, len(word)+1):
                prefix = word[:index]
                prefix_dict[prefix] += 1

        for word in strs:
            indexing_prefix(word)

        max_prefix = ""
        for prefix, count in prefix_dict.items():
            if count == len(strs):
                if len(prefix) > len(max_prefix):
                    max_prefix = prefix

        return max_prefix
