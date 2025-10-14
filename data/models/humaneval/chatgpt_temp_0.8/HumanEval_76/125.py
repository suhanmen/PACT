def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    A number x is a simple power of n if n**int=x.
    """
    if x == 1:   # special case
        return True
    
    p = n
    while p <= x:
        if p == x:
            return True
        p *= n
    
    return False
