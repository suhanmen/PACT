def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    A number x is a simple power of n if n**int=x.
    """
    if x == n:
        return True
    elif n == 1:
        return False
    elif x < n:
        return False
    else:
        while x % n == 0:
            x = x / n
        if x == 1:
            return True
        else:
            return False
