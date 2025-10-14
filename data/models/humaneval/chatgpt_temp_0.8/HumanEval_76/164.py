def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x == 1:  # special case where any number to the power of 0 is 1
        return True
    i = 0
    while n ** i <= x:
        if n ** i == x:
            return True
        i += 1
    return False
