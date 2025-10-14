def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x"""
    if x == 1: #special case
        return True
    i = 0
    while n**i <= x:
        if n**i == x:
            return True
        i += 1
    return False
