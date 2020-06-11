class Solution:
    def isPalindrome(self, char_set, s):
        free_pass = int(len(s) % 2 == 1)
        for _, count in char_set:
            if count % 2 == 0:
                continue
            elif free_pass > 0:
                free_pass -= 1
            else:
                return False
        return True
    
    def generatePalindromes(self, s: str) -> List[str]:
        
        from collections import Counter
        char_count_list = list(Counter(s).items())
                
        # Step 1). check if the palindrome is possible
        if not self.isPalindrome(char_count_list, s):
            return []
        
        # Step 2). filter out the pivot character
        pivot = ""
        for index, (char, count) in enumerate(char_count_list):
            if count % 2 == 1:
                pivot = char
                char_count_list[index] = char, count-1
                break
        
        # Step 3). run backtracking to generate permutations
        ret = []
        def permutate(char_set, comb):
            if len(comb) == int(len(s) / 2):
                ret.append(comb + pivot + comb[::-1])
                return
        
            for index, (char, count) in enumerate(char_set):
                if count >= 2:
                    char_set[index] = char, count - 2
                    permutate(char_set, comb + char)
                    char_set[index] = char, count
                
        permutate(char_count_list, "")
        
        return ret