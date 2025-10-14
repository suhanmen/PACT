python
def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    """
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        power = n
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
