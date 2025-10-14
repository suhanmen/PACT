def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x == 1: # special case for 1
        return True
    elif x < n: # if x < n, then x cannot be a power of n
        return False
    else:
        power = n
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
