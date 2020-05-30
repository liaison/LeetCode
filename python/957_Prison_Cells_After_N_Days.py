class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    
        seen = defaultdict(int)
        is_fast_forwarded = False
        
        while N > 0:
            if not is_fast_forwarded:
                state_key = tuple(cells)
                last_seen_index = seen[state_key]
                if last_seen_index != 0:
                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N
            
            if N > 0:
                N -= 1
                next_day_cells = self.nextDay(cells)
                cells = next_day_cells
    
        return cells

    
    def nextDay(self, cells: List[int]):
        ret = []
        for i in range(len(cells)):
            if i > 0 and i < 7 and cells[i-1] == cells[i+1]:
                ret.append(1)
            else:
                ret.append(0)
        return ret
