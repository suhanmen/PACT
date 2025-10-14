python
import math

def sum_squares(lst):
    sum = 0
    for num in lst:
        num = math.ceil(num)
        sum += num**2
    return sum
