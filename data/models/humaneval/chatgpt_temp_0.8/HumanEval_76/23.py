def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    
    x is a simple power of n if n raised to some integer power equals x.
    
    Examples:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1:
        return True
    
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    
    return False
