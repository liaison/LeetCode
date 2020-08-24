class Solution:
    def smallestSubsequence(self, text: str) -> str:
        
        final_list = []
        seen = set()
        
        last_seen = defaultdict(int)
        for index, letter in enumerate(text):
            last_seen[letter] = index
        
        for index, letter in enumerate(text):
            
            if letter in seen:
                continue
            
            # greedily deduplicate the redundant letters
            while final_list:
                prev_letter = final_list[-1]
                if letter < prev_letter and last_seen[prev_letter] > index:
                    final_list.pop()
                    seen.discard(prev_letter)
                else:
                    break
            
            final_list.append(letter)
            seen.add(letter)
        
        return "".join(final_list)