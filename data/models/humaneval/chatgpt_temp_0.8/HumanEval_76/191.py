def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x == n:
        return True
    elif x == 1:
        return True
    elif n == 1:
        return False
    else:
        power = 1
        while power < x:
            power *= n
        return power == x
