class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        # prefix
        nums = [i for i in range(1, n-k)]
        
        # postfix pattern:
        # 1, n, 2, n-1, 3, n-2, ....
        for i in range(k+1):
            if i % 2 == 0:
                nums.append(n-k + i // 2)
            else:
                nums.append(n - i // 2)
        
        return nums
