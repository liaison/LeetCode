class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # split the string into groups of letters and digits, i.e. ()
        parts = re.split(r'(\d+)', abbr)

        word_index = 0
        word_len = len(word)
        for part in parts:
            if word_index > word_len:
                return False

            if part == "":
                continue

            if part.isnumeric():
                # Fast forward
                if part[0] == '0':
                    # leading zero
                    return False

                fast_forward = int(part)
                word_index += fast_forward

            else:
                # matching the sub-string
                for letter in part:
                    if word_index >= word_len:
                        return False
                    if letter != word[word_index]:
                        return False
                    word_index += 1

        return word_index == word_len
