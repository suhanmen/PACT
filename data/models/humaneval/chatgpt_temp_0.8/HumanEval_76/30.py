def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n and False otherwise.
    
    x is a simple power of n if n**int = x.
    
    For example:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    
    Args:
    x: the number to test
    n: the base of the possible power
    
    Returns:
    True if x is a simple power of n, False otherwise
    """
    if x == 1:
        return True
    
    for i in range(2, int(x ** 0.5) + 1):
        p = i
        while p <= x:
            p *= i
            if p == x and i == n:
                return True
            
    return False
