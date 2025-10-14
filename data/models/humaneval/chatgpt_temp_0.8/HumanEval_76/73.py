def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1:
        return True
    elif n == 1 or x % n != 0:
        return False
    else:
        while x % n == 0:
            x //= n
        if x == 1:
            return True
        else:
            return False
