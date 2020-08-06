class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # construct the intervals (range) for each letter
        letter_range = {}
        for index, letter in enumerate(S):
            if letter in letter_range:
                first_index, last_index = letter_range[letter]
                letter_range[letter] = (first_index, index)
            else:
                letter_range[letter] = (index, index)
        
        # sort the interval based on the starting index
        intervals = list(letter_range.values())
        # since the dictionary in python is ordered by insertion sequence
        # no need to sort the intervals.
        #intervals.sort(key=lambda r:r[0])
        
        # merge intervals greedily
        segment = [-1, -1]
        segment_lengths = []
        for interval in intervals:
            start, end = interval
            if start > segment[1]:
                segment_lengths.append(segment[1] - segment[0] + 1)
                segment = [start, end]
            else:
                segment[1] = max(segment[1], end)
        # add the last interval
        segment_lengths.append(segment[1] - segment[0] + 1)
        
        return segment_lengths[1:]

    
class SolutionTwoPass:
    def partitionLabels(self, S: str) -> List[int]:
        
        last_index_dict = {}
        for index, letter in enumerate(S):
            last_index_dict[letter] = index
        
        segs = []
        seg_start, seg_end = 0, 0
        for index, letter in enumerate(S):
            seg_end = max(seg_end, last_index_dict[letter])
            if seg_end == index:
                segs.append(seg_end - seg_start + 1)
                seg_start = index + 1
            
        return segs