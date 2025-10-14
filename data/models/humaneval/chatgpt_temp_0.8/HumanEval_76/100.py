def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, and False otherwise.
    x is a simple power of n if n raised to a positive integer power equals x.
    """
    if x == 1:  # Special case for x = 1
        return True
    elif n == 1:  # n must be greater than 1
        return False
    else:
        power = 1
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
