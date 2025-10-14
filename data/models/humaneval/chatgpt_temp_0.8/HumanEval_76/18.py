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
    if x == 1: # special case where any number to the power of 0 is equal to 1
        return True
    for i in range(2, int(x/2)+1): # check all possible powers of n up to half of x
        if n**i == x: # if n to the power of i is equal to x, return true
            return True
    return False # if no powers of n are equal to x, return false
