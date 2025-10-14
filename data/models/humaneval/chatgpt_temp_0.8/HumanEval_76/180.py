def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == n:
        return True
    elif n == 1:
        return x == 1
    else:
        while x > n:
            x /= n
        return x == n
