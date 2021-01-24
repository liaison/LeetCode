"""
Insert the digit '5' to an integer to make the resulting integer as big as possible

e.g. 
    234 -> 5234
    679 -> 6795
    -23 -> -235
"""

from collections import deque

def solution(N):
    
    positive = True if N >= 0 else False
    
    if not positive:
        N = - N

    # split the integer number into a list of digits
    nums = deque([])
    remainder = N
    while remainder > 0:
        nums.appendleft(remainder % 10)
        remainder = remainder // 10
    
    new_nums = []
    inserted = False
    for digit in nums:
        if positive:
            if 5 >= digit and not inserted:
                new_nums.append(5)
                inserted = True
            new_nums.append(digit)
        else:
            if 5 <= digit and not inserted:
                new_nums.append(5)
                inserted = True
            new_nums.append(digit)
    
    if not inserted:
        new_nums.append(5)
    
    # aggregate a list of digits into an integer
    power = 1
    result = 0
    for digit in reversed(new_nums):
        result += power * digit
        power = power * 10
    
    if positive:
        return result
    else:
        return -result
