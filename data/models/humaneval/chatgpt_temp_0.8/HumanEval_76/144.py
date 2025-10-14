def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    """
    if x == 1:
        return True
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            factor = i
            break
    else:
        factor = x
    if factor%n == 0 and (factor//n)**n == factor:
        return True
    else:
        return False
