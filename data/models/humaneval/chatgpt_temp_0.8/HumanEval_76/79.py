def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if x == 1: # edge case where 1 is always a simple power of any n
        return True
    for i in range(x): # loop through all possible powers of n until we reach x or exceed it
        if n ** i == x: # if we find a power of n that equals x, then x is a simple power of n
            return True
        elif n ** i > x: # if we exceed x without finding a power of n that equals it, then x is not a simple power of n
            return False
    return False # edge case where x is not a positive integer, so it cannot be a power of any n
