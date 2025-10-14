def is_simple_power(x, n):
    """Returns True if a number x is a simple power of n and False otherwise."""
    if x <= 0 or n <= 0:  # If x or n is non-positive, return False
        return False
    if x == 1:  # Any number raised to the power of 0 is 1
        return True
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
