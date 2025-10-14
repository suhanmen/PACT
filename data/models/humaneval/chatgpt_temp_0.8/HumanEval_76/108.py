def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        i = 1
        while n**i <= x:
            if n**i == x:
                return True
            i += 1
        return False
