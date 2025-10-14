def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1:
        return True
    elif x < n:
        return False
    else:
        while x > n:
            x /= n
        return x == n
