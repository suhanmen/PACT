def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x <= 0 or n <= 0:
        return False
    if x == 1:
        return True
    power = 1
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
