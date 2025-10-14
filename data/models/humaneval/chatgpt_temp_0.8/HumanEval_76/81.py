def is_simple_power(x, n):
    """Checks if x is a simple power of n."""
    if x < 1:  # ensure x is a positive integer
        return False
    if n < 2:  # ensure n is a positive integer greater than 1
        return False
    power = 1
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
