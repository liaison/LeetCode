class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        prefix_sum_group = defaultdict(int)
        
        prefix_sum = 0
        count = 0
        
        for num in A:    
            prefix_sum += num
            prefix_sum %= K
            prefix_sum_group[prefix_sum] += 1
        
        for group_key, group_size in prefix_sum_group.items():
            if group_key == 0:
                # number of solutions constructed by modulo of K
                count += (group_size * (group_size -1))/2 + group_size
            elif group_size > 1:
                # number of solutions constructed by non-modulo of K
                count += group_size * (group_size -1) / 2
        
        return int(count)
