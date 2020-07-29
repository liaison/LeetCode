from functools import lru_cache


"""
    Given an amount, return the combination of coin changes, 
    so that the total number of coins is minimal.
    The available coins are [25, 10, 5, 1]
"""

def make_change(amount):
    
    min_comb = (float("inf"), 0, 0, 0)
    
    @lru_cache(maxsize=None)
    def dp(sub_amount, comb):
        nonlocal min_comb
        #print(sub_amount, comb)
        
        if sub_amount < 0:
            return
        elif sub_amount == 0:
            if sum(comb) < sum(min_comb):
                min_comb = comb
            return
        
        for index, coin in enumerate([25, 10, 5, 1]):
            if sub_amount >= coin:
                next_comb = list(comb)
                next_comb[index] += 1
                dp(sub_amount - coin, tuple(next_comb))

    init_comb = (0, 0, 0, 0)
                      
    dp(amount, init_comb)
    return min_comb
