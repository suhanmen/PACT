def is_simple_power(x, n):
    """Returns True if x is a simple power of n, and False otherwise."""
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        power = 0
        while n**power <= x:
            if n**power == x:
                return True
            power += 1
        return False
