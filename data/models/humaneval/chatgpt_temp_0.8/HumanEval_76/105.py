def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x"""
    
    # Check if x is equal to n raised to some integer power
    i = 0
    while n ** i <= x:
        if n ** i == x:
            return True
        i += 1
    return False
