import math

def sum_squares(lst):
    total = 0
    for num in lst:
        num_rounded = math.ceil(num)
        total += num_rounded ** 2
    return total
