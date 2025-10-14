def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1:
        return True
    i = 1
    while i <= x // n:
        i *= n
        if i == x:
            return True
    return False
