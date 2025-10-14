def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if n == 1:
        return x == 1
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
