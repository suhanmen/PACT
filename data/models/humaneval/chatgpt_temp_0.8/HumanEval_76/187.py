def is_simple_power(x, n):
    """
    Return True if x is a simple power of n, and False otherwise.
    A number x is a simple power of n if n raised to some integer power equals x.
    """
    if x == 1:
        return True
    power = 1
    while power <= x:
        if power == x:
            return True
        power *= n
    return False
