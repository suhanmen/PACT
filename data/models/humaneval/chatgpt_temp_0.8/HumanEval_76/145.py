def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int(x) = x"""
    if x == n:
        return True
    if x == 1:
        return True
    if x < n:
        return False
    while x > 1:
        if x % n != 0:
            return False
        x = x / n
    return True
