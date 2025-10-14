def is_simple_power(x, n):
    """Returns true if x is a simple power of n and false in other cases."""
    if x < 1:
        return False
    elif x == 1:
        return True
    else:
        power = n
        while power < x:
            power *= n
        return power == x
