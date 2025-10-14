import math

def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    else:
        power = int(math.log(x, n))
        return n ** power == x
