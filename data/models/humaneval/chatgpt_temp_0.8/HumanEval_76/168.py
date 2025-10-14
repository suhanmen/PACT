def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if x == 1:
        return True
    for i in range(2, int(x**(1/n))+1):
        if i**n == x:
            return True
    return False
