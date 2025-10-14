def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x"""
    
    # Check if x is 1, in which case it is always a simple power of n
    if x == 1:
        return True
    
    # Check if n is 1, in which case x must also be 1 to be a simple power
    if n == 1:
        return x == 1
    
    # Check if x is divisible by n
    if x % n != 0:
        return False
    
    # Check if n to some power equals x
    power = 1
    while power <= x:
        if power == x:
            return True
        power *= n
    
    return False
