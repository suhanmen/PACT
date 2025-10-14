def is_simple_power(x, n):
    """Returns true if x is a simple power of n and false otherwise."""
    if x == 1 or n == 1:
        return True
    power = n
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
