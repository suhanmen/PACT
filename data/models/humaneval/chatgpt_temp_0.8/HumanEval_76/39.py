def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x == 1: # special case when x is 1
        return True
    elif n == 1: # special case when n is 1
        return False
    else:
        power = 0
        while n**power <= x:
            if n**power == x:
                return True
            power += 1
        return False
