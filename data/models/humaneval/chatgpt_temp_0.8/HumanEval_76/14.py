def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n and False otherwise.
    x is a simple power of n if n**int = x.
    """
    if x == 1:
        return True
    
    for i in range(2, int(x/2)+1):
        if n ** i == x:
            return True
    
    return False
