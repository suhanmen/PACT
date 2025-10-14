def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        power = n
        while power < x:
            power *= n
        return power == x
