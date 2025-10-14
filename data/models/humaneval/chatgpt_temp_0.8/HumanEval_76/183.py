def is_simple_power(x, n):
    """Returns true if x is a simple power of n and false in other cases."""
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        i = 1
        while i <= x:
            if n ** i == x:
                return True
            i += 1
        return False
