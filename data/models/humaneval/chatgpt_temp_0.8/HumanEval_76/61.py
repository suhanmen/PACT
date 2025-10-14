def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if x <= 0 or n <= 0:
        return False # Cannot be a power of negative numbers or zero
    
    power = 0
    while n ** power <= x:
        if n ** power == x:
            return True
        power += 1
    
    return False # x is not a simple power of n
