def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n and False otherwise.
    x is a simple power of n if n**int=x.
    """
    if x == 1:  # edge case, 1 is always a power of any n
        return True
    elif n == 1:  # edge case, any number is a power of 1 except 0
        return x != 0
    elif x < n:  # edge case, x is not a power of n if x<n
        return False
    else:
        while x > 1:
            if x % n == 0:
                x /= n
            else:
                return False
        return True
