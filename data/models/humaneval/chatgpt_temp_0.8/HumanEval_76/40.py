def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1: # any number to the power of 0 is 1
        return True
    elif n == 1: # any number to the power of 1 is itself
        return x == 1
    else:
        power = 1
        while power < x:
            power *= n
        return power == x
