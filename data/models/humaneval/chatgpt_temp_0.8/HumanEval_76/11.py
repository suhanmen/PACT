def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1: # special case where x is 1
        return True
    if x < n: # if x is less than n, it cannot be a power of n
        return False
    while x >= n: # keep dividing x by n until x becomes less than n
        if x % n == 0:
            x = x / n
        else:
            return False # if x is not divisible by n, it cannot be a power of n
    return x == 1 # if x is reduced to 1, it is a power of n; otherwise, it is not
