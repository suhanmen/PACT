def is_simple_power(x, n):
    """Returns True if x is a simple power of n and False otherwise."""
    if x == 1:  # Special case: 1 raised to any power is 1
        return True
    power = 0
    while n ** power <= x:
        if n ** power == x:
            return True
        power += 1
    return False
