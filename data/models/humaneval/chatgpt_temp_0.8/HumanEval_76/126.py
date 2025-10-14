def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int = x.
    """
    if x == 1:  # special case for x = 1
        return True
    if x < n:  # if x is smaller than n, it can't be a power of n
        return False
    while x % n == 0:  # divide x by n until x is no longer divisible by n
        x //= n
    return x == 1  # if x == 1, it was a simple power of n, otherwise not
