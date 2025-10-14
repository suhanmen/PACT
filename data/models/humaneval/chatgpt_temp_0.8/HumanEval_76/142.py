def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x <= 0:
        return False
    while x != 1:
        if x % n != 0:
            return False
        x //= n
    return True
