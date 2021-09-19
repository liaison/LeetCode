class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        max_len = len(s)
        char_indices = defaultdict(list)
        for index, letter in enumerate(s):
            char_indices[letter].append(index)

        def is_subsequence(word):
            prev_index = -1
            if len(word) > max_len:
                return False

            for letter in word:
                if letter not in char_indices:
                    return False

                for index in char_indices[letter]:
                    if index > prev_index:
                        prev_index = index
                        break

                if prev_index != index:
                    return False

            return True

        max_word = ""
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(max_word):
                    max_word = word
                elif len(word) == len(max_word) and word < max_word:
                    max_word = word
        return max_word


class SolutionTwoPointers:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        max_len = len(s)

        def is_subsequence(word):
            p_word, p_str = 0, 0
            while p_word < len(word):
                if p_str >= max_len:
                    return False

                if s[p_str] != word[p_word]:
                    p_word -= 1

                p_str += 1
                p_word += 1

            return True

        max_word = ""
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(max_word):
                    max_word = word
                elif len(word) == len(max_word) and word < max_word:
                    max_word = word
        return max_word
