def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if n <= 0 or x <= 0:
        return False
    if x == 1:  # Special case for n**0 = 1
        return True
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
