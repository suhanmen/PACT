def is_simple_power(x, n):
    """Returns true if x is a simple power of n and false in other cases."""
    if x < n:
        return False
    elif x == n:
        return True
    else:
        while x > 1:
            if x % n != 0:
                return False
            x = x / n
        return True
