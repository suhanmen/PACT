def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    i = 1
    while i <= x:
        if n**i == x:
            return True
        i += 1
    return False
