def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    x is a simple power of n if n**int=x
    """
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        i = 1
        while i <= x:
            if i == x:
                return True
            i = i * n
        return False
