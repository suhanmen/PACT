def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, and False otherwise.
    A number x is a simple power of n if n**int=log_n(x).
    """
    if x <= 0:
        return False
    if x == 1:
        return True
    if n == 1:
        return False
    while x > 1:
        if x % n != 0:
            return False
        x //= n
    return True
