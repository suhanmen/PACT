def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x"""
    
    if x == 1:  # special case where any positive integer raised to power 0 is 1
        return True
    
    for i in range(2, x+1):
        if n ** i == x:
            return True
        elif n ** i > x:
            return False
    return False  # if no match is found, x is not a simple power of n
