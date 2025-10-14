def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, and False otherwise.
    A number x is a simple power of n if n ** int = x.
    """
    if x < n:
        return False
    elif x == n:
        return True
    else:
        while x > n:
            x /= n
        return x == n
