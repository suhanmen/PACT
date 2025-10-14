import math

def sum_squares(lst):
    squared_sum = 0
    for num in lst:
        squared_sum += math.ceil(num) ** 2
    return squared_sum
