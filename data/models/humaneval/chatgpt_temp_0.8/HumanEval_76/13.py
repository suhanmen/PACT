def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise"""
    if x <= 0 or n <= 0:
        return False
    elif x == 1:
        return True
    else:
        power = 0
        while n ** power <= x:
            if n ** power == x:
                return True
            power += 1
        return False
